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

    # delete any category saved (resets search results)
    if 'category' in request.session:
        del request.session['category']

    return render(request, 'index.html', context)

def search(request):
    if request.method == 'GET':
        return redirect('/')

    print(request.POST)

    # default context
    context = {
        'products' : Product.objects.all()
    }

    # categorize
    if 'category' in request.POST:
        request.session['category'] = request.POST['category'] # Set category for future reference
        context['products'] = Product.objects.filter(category = request.session['category'])
    # search with category
    elif 'Search' in request.POST and 'category' in request.session:
        context['products'] = Product.objects.filter(name__icontains = request.POST['Search'], category = request.session['category'])
    # search no category
    else:
        context['products'] = Product.objects.filter(name__icontains = request.POST['Search'])
    
    # if context['products']:
    #     print("found products")
    # else:
    #     print("no products")

    return render(request, 'partials/searchResult.html', context)