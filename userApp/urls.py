from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('register/createUser/', views.createUser),
    path('login/', views.login),
    path('sampleLogin/', views.sampleLogin),
    path('logout/', views.logout),
    path('profile/', views.profile),
    path('wishlist/', views.wishlist),
    path('wishlist/removeProduct/<productid>', views.remove_from_wishlist),
    path('wishlist/addProduct/<productid>', views.add_to_wishlist),
]