from django.shortcuts import render, redirect
import re

from .models import *
from userApp.models import User

def index(request):
    context = {
        'products' : Product.objects.all()
    }

    # TODO: set up html based on user object
    # place user (if any)
    # if 'userid' in request.session:
    #     context['user'] = User.objects.get(id=request.session['userid'])

    # delete any category saved (resets search results)
    if 'category' in request.session:
        del request.session['category']

    return render(request, 'index.html', context)

def search(request):
    # default context
    context = {
        'products' : Product.objects.all()
    }

    # categorize
    if 'category' in request.POST:
        request.session['category'] = request.POST['category'] # Set category for future reference
        context['products'] = Product.objects.filter(category = request.session['category'])
    # search (with category)
    elif 'Search' in request.POST and 'category' in request.session:
        context['products'] = Product.objects.filter(name__icontains = request.POST['Search'], category = request.session['category'])
    # search (no category)
    elif 'Search' in request.POST:
        context['products'] = Product.objects.filter(name__icontains = request.POST['Search'])
    # else a GET request was made (or a vield name was altered):
        # use default context
    
    # serve up search results
    return render(request, 'partials/searchResult.html', context)