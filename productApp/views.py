from django.shortcuts import render, redirect

from .models import *
# from ..userApp.models import User

def index(request):
    # if 'userid' in request.session:
    #     context = {
    #         'user' : User.objects.get(id=request.session['userid'])
    #     }
    #     print(context['user'])

    context = {
        'products' : Product.objects.all()
    }

    return render(request, 'index.html', context)