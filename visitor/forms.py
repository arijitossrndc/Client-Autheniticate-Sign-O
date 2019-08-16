from django import forms
from .models import UserRegistration
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    UserName = forms.CharField(
        required=True,
        label='UserName',
        max_length=50
    )
   
    Password = forms.CharField(
        required=True,
        label='Password',
        max_length=100,
        widget=forms.PasswordInput()
    )
    