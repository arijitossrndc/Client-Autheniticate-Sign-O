from django import forms
from .models import UserRegistration


class register_form_org(forms.ModelForm):
    class Meta:
        model = UserRegistration

        fields = ('UserName','Password','ConfirmPassword','Name','Salt','StartDate','ExpiredDate','Amount','Email','MobileNo')
    
class login_form_org(forms.ModelForm):
	class Meta:

		model = UserRegistration

		fields = ('UserName','Password')