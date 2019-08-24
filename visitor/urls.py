from django.urls import path
from . import views
from .views import register,create

urlpatterns = [
    path('register',views.register),
    path('create',views.create),


    ]
