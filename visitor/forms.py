from django import forms
from .models import UserRegistration
from django.contrib.auth.models import User

class login_form_org(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'
    
    