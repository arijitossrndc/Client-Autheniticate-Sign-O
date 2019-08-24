from django.urls import path
from . import views
from .views import register,create,login,logout

urlpatterns = [
    path('register',views.register),
    path('create',views.create),
    path('login',login),
    path('logout',logout),


    ]
