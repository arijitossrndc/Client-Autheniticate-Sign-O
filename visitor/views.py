
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from.models import UserRegistration
from .forms import login_form_org



# register user


# register user
def register(request):
	return render(request,"visitor/login_org.html")

def create(request):

	if request.method == 'GET':
		
		form = login_form_org()

		return render(request,'visitor/login_org.html',{'form':form})

	if request.method == 'POST':
		form = login_form_org(request.POST)
		if form.is_valid():
			UserName = form.cleaned_data['UserName']
			password = form.cleaned_data['Password']
			confirm_password = form.cleaned_data['confirm_password']
			if(password==confirm_password):
				form.save()
				form = login_form_org()
				success = "Registered success"
				context = {
				'not':success,
				'form':form
				}
			else:
				form = login_form_org()
				error = "password and confirm password doesnot not match"
				context={
				'not':error,
				'form':form
				}
		
		return render(request,'visitor/login_org.html',context)



    
