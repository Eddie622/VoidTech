from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
import bcrypt

# registration page
def register(request):
    return render(request, 'register.html')

# crate user route
def createUser(request):
    print(request.POST)
    if request.method == "GET":
        return redirect("../")
    
    # validate fields on back-end
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect("../")
    else:
        # hash password
        password = request.POST['pwd']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        # create user
        User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=pw_hash)
        return redirect("/")

# login route
def login(request):
    if request.method == "GET":
        return redirect("/")
    
    # find user in database
    user = User.objects.filter(email=request.POST['email'])
    # if user exists
    if user:
        logged_user = user[0]
        # verify password
        if bcrypt.checkpw(request.POST['pwd'].encode(), logged_user.password.encode()):
            # place user in session
            request.session['userid'] = logged_user.id
            request.session['fname'] = logged_user.first_name
            # if remember me activated, save email, else delete session data for email
            if 'remember' in request.POST:
                request.session['email'] = logged_user.email
            else:
                if 'email' in request.session:
                    del request.session['email']
            return redirect("/")
    
    # user does not exist
    messages.error(request,'invalid email/password')
    return redirect("/")

#logout route
def logout(request):
    # if user is logged in, clear user specific session variables
    if 'userid' in request.session:
        del request.session['userid']
        del request.session['fname']
    return redirect('/')