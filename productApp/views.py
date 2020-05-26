from django.shortcuts import render, redirect
# from ..userApp.models import User

def index(request):
    # if 'userid' in request.session:
    #     context = {
    #         'user' : User.objects.get(id=request.session['userid'])
    #     }
    #     print(context['user'])
    return render(request, 'index.html')