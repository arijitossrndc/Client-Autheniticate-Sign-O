
from django.shortcuts import render, HttpResponseRedirect, reverse,  redirect, HttpResponse
from .models import UserRegistration
from .forms import login_form_org,register_form_org
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from django.urls import reverse



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
			confirm_password = form.cleaned_data['ConfirmPassword']
			Name = form.cleaned_data['Name']
			Salt = form.cleaned_data['Salt']
			StartDate = form.cleaned_data['StartDate']
			ExpiredDate = form.cleaned_data['ExpiredDate']
			Amount = form.cleaned_data['Amount']
			Email =form.cleaned_data['Email']
			MobileNo = form.cleaned_data['MobileNo']

		
			if(password==confirm_password):
				form.save()

				form = login_form_org()
				success = "Registered success"
				context = {
				'not':success,
				'form':form,
				}
				return HttpResponseRedirect("create")
			else:
				form = login_form_org()
				error = "password and confirm password doesnot not match"
				context={
				'not':error,
				'form':form,
				}
		
		return render(request,'visitor/login_org.html')

def login(request):

	form =login_form_org()


	if request.method == "GET":

		if request.session.has_key('company'):

			username = request.session['company']
			error = "welcome back"
			context = {
			'username':username,
			'error':error,
			'form':form,
			}
			return render(request,'visitor/login_org.html',context)
		else:
			error ="Please login"
			context = {
			'form':form,
			'error':error,
			}
		return render(request,'visitor/login_org.html',{'form':form})
	else:

		form = login_form_org(request.POST)
		if form.is_valid():

			company = request.POST['UserName']
			password = request.POST['Password']

			Check = UserRegistration.objects.filter(UserName=company,Password=password).count()

			if(Check>=1):
				request.session['company']=company
				context={
				'username':company,
				'form':form,
				}
				return render(request,'visitor/login_org.html',context)
			else:
				error="please login"
				context={
				'error':error,
				'form':form,
				}

				return render(request,'visitor/login_org.html',context)
		

def logout(request):
	form = login_form_org()

	del request.session['company']
	context={
	'form':form,
	}
	return render(request,'visitor/login_org.html',context)



class UserRegistrationList(APIView):

	def get(self, request):

		UserRegistration1 = UserRegistration.objects.all()

		serializer = UserRegistrationSerializer(UserRegistration1, many=True)

		return Response(serializer.data)

	def post(self):
		pass

