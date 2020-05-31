from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.search),
    path('cart/', views.view_cart),
    path('cart/addProduct/<int:productid>/', views.add_to_cart),
    path('cart/removeProduct/<int:productid>/', views.remove_from_cart)
]