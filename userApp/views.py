# TODO: On registration page,
# show error messages when back-end validation fails (use bootstrap validation), 
# also alert user on succesful account creation
# TODO: DONT USE userid IN ROUTE!!!!!!!!!!!

from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from productApp.models import Product
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
        new_user = User.objects.create(first_name=request.POST['fname'],last_name=request.POST['lname'],email=request.POST['email'],password=pw_hash)
        # create user wishlist
        Wishlist.objects.create(user = new_user)
        # create user cart
        Cart.objects.create(user = new_user)
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

# sample login route
def sampleLogin(request):
    # find user in database
    user = User.objects.filter(email='sample@email.com')
    # if user exists
    if user:
        logged_user = user[0]
        # verify password
        if bcrypt.checkpw('samplePass'.encode(), logged_user.password.encode()):
            # place user in session
            request.session['userid'] = logged_user.id
            # delete session data for email
            if 'email' in request.session:
                del request.session['email']
            return redirect("/")
    
    # user does not exist
    messages.error(request,'invalid email/password')
    return redirect("/")

# logout route
def logout(request):
    # if user is logged in, clear user specific session variables
    if 'userid' in request.session:
        del request.session['userid']
    return redirect('/')

# user profile route
def profile(request):
    if 'userid' not in request.session:
        return redirect('/')
    
    context = {
        'user' : User.objects.get(id=request.session['userid'])
    }

    return render(request, "profile.html", context)

# user wishlist route
def wishlist(request):
    if 'userid' not in request.session:
        return redirect('/')

    context = {
        'user' : User.objects.get(id=request.session['userid'])
    }

    return render(request, "wishlist.html", context)

# remove product from wishlist route
def remove_from_wishlist(request, productid):
    if 'userid' not in request.session:
        return redirect('/')
    
    # get the user's wishlist
    user_wishlist = Wishlist.objects.get(user_id=request.session['userid'])
    # remove product selected from user's wishlist
    user_wishlist.products.remove(Product.objects.get(id=productid))

    return redirect(f"/user/wishlist/")

# add product to wishlist route
def add_to_wishlist(request, productid):
    if 'userid' not in request.session:
        return redirect('/')
    
    # get the user's wishlist
    user_wishlist = Wishlist.objects.get(user_id=request.session['userid'])
    # add product selected to user's wishlist
    user_wishlist.products.add(Product.objects.get(id=productid))

    return redirect(f"/user/wishlist/")

# def add_to_cart(request, productid):
#     if not uverifyUser()
    
#     # get the user's cart
#     user_cart = Cart.objects.get(user_id=request.session['userid'])
#     # add product selected to user's cart
#     user_cart.products.add(Product.objects.get(id=productid))

#     return redirect(f"/user/cart/")