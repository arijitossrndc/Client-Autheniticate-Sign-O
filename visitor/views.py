
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from.models import UserRegistration
from .forms import UserRegistrationForm



# register user


# register user
def register(request):
	return render(request,"visitor/login_org.html")

def create(request):

	form  =  UserRegistrationForm(request.POST)

	if request.method == 'POST':

		if form.is_valid():

			UserName = form.cleaned_data['UserName']
			Password = form.cleaned_data['Password']
			form.save()

	return redirect('visitor/register')



    
