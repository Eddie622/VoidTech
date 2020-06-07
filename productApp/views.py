#TODO: On index route, display alert message when product is added to wishlist/cart with ajax

from django.shortcuts import render, redirect
import re

from .models import *

# homepage
def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = []

    context = {
        'products' : Product.objects.all(),
        'cart_total' : len(request.session['cart'])
    }

    # place user (if any)
    if 'userid' in request.session:
        context['user'] = User.objects.get(id=request.session['userid'])

    # delete any category saved (resets search results)
    if 'category' in request.session:
        del request.session['category']

    return render(request, 'index.html', context)

# search products
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
    # else a GET request was made (or a field name was altered):
        # will use default context
    
    # serve up search results
    return render(request, 'partials/searchResult.html', context)

# add product to cart route
def add_to_cart(request, productid):
    # generate cart if not exists
    if 'cart' not in request.session:
        request.session['cart'] = []
    
    # append product & save
    request.session['cart'].append(productid)
    request.session.save()

    return redirect("/")

# remove product from cart route
def remove_from_cart(request, productid):
    if 'cart' not in request.session:
        return redirect("/")
    
    # remove product and save
    request.session['cart'].remove(int(productid))
    request.session.save()

    return redirect("/cart/")

# checkout route
def view_cart(request):
    # Grab all product objects in cart
    cart_products = []
    for productid in request.session['cart']:
        cart_products.append(Product.objects.get(id=productid))

    context = {
        'cart_products' : cart_products,
        'cart_total' : len(cart_products)
    }

    return render(request, 'checkout.html', context)