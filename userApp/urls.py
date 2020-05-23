from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('register/createUser/', views.createUser),
    path('login/', views.login),
    path('logout/', views.logout),
]