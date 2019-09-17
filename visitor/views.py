
from django.shortcuts import render, HttpResponseRedirect, reverse,  redirect, HttpResponse
from .models import UserRegistration, Departments,Employee
from .forms import login_form_org,register_form_org,department_form_org
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from django.urls import reverse
from django.contrib.auth.hashers import check_password
from django.conf import settings

# register user


# register user
def register(request):
    return render(request,'client/register_org.html')

def create(request):

    if request.method == 'GET':

        if request.session.has_key('register'):
            print(request.session['register'])
            return HttpResponseRedirect("login")
        else:
            form = register_form_org()
            return render(request,'client/register_org.html',{'form':form,'error':"please register",})


    if request.method == 'POST':
        form = register_form_org(request.POST)
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

            r = UserRegistration.objects.filter(UserName=UserName).count()
            if password == confirm_password and r==0:
                print("hurray")
                request.session['register'] = UserName
                form.save()
                form = register_form_org()
                success = "Registered success"
                context = {
                'not': success,
                'form': form,
                }
                return render(request,'client/register_org.html',{'form':form,'error':"Registered success",})
           
            else:
                form = register_form_org()
                error = "password and confirm password doesnot not match or username already taken"
                context={
                'not': error,
                'form': form,
                }

        return render(request, 'client/register_org.html',{'error':"password and confirm password doesnot not match or username already taken",'form':form,},)

def login(request):

    form =login_form_org()


    if request.method == "GET":

        if request.session.has_key('company'):

            username = request.session['company']

            error = "welcome " + username
            context = {
            'username':username,
            'error':error,
            'form':form,
            'User':request.session['id'],
            }
            return render(request,'client/department.html',context)
        else:
            error ="Please login"
            context = {
            'form':form,
            'error':error,
            }
        return render(request,'client/login_org.html',{'form':form,'error':error,})
    else:

        form = login_form_org(request.POST)
        if form.is_valid():

            company = request.POST['UserName']
            password = request.POST['Password']
            print("sagar")

            Check = UserRegistration.objects.filter(UserName=company).count()

            if Check>=1:

                u = UserRegistration.objects.get(UserName=company)
                HashedPassword = u.Password
                print(check_password(password, u.Password))


                if  check_password(password, u.Password):
                    print(check_password(password, u.Password))
                    print("vaaa")
                    request.session['company'] = company
                    error = "you logged in " + company
                    query_set = UserRegistration.objects.get(UserName = company)
                    query_set = query_set.Id
                    request.session['id'] = query_set
                    return render(request,'client/department.html',{ 'username':company,'form':form,'error':error,'User':query_set,})

    return render(request,'client/login_org.html',{'error':'please login','form':form,})

def logout(request):
    error = "you logged out succesfully"
    if 'register' in request.session:
        del request.session['register']
    if 'company' in request.session:
        del request.session['company']


    return HttpResponseRedirect("login")

def AddDepartment(request):

    if request.session.has_key('company'):
        username = request.session['company']
        if request.method == 'POST':
            form = department_form_org()
            name = request.POST['DepartmentName']
            print(name)

            d = UserRegistration.objects.get(UserName=username,Id=request.session['id'])
            d =d.Id
            b = Departments(UserId_id = d, DepartmentName = name,)
            b.save()
            context={
                'username': username,
                'form': form,
                'User':request.session['id'],
            }

            form = department_form_org()
            return render(request,'client/department.html',{'form': form,'username':username,'User':request.session['id'],'error': "department added succesfully!!",})

def AddEmployee(request):


    if request.session.has_key('company'):
        username = request.session['company']
        form = department_form_org()

        if request.method == 'POST':

            Name = request.POST['Name']
            Email = request.POST['Email']
            MobileNo = request.POST['MobileNo']
            Address = request.POST['Address']
            name = request.POST['DepartmentName']

            u =UserRegistration.objects.get(UserName=username)
            u=u.Id
            d =Departments.objects.get(UserId = u, DepartmentName=name )
            d = d.Id
            e =Employee(Name = Name, MobileNo=MobileNo,Address=Address,EmailId=Email,UserId_id = u, DepartmentId_id = d)
            e.save()
            form = department_form_org()
            return render(request,'visitor/department.html',{'form': form,'username':username,'User':request.session['id'],'error':"employee added succesfully!!",})
            


class UserRegistrationList(APIView):

     def get(self, request):

        UserRegistration1 = UserRegistration.objects.all()

        serializer = UserRegistrationSerializer(UserRegistration1, many=True)

        return Response(serializer.data)

     def post(self):
         pass

