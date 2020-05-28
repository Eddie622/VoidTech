from django.shortcuts import render, redirect
import re

from .models import *
from userApp.models import User

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

def search(request):
    context = {
        'products' : Product.objects.filter(name__icontains = request.POST['Search'])
    }

    if context['products']:
        print("found products")
    else:
        print("no products")

    return render(request, 'partials/searchResult.html', context)