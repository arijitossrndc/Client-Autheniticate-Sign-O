from django.urls import path
from .views import register,create

urlpatterns = [
    path('register',register),
    path('create',create),


    ]
