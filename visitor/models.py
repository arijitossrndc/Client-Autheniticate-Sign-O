from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator
# Create your models here.
class UserRegistration(models.Model):
    Id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50, null=False)
    Password = models.CharField(max_length=100, null=False)
    ConfirmPassword = models.CharField(max_length=100, null=False)
    Name = models.CharField(max_length=50, null=True)
    Salt = models.CharField(max_length=20, null=True)
    isDeleted = models.BooleanField(null=True, default=False)
    StartDate = models.DateTimeField(default=timezone.now)
    ExpiredDate = models.DateTimeField(default=timezone.now)
    Amount = models.DecimalField(null=True, max_digits=12,validators=[MinValueValidator(0),], decimal_places=4)
    EmailService = models.BooleanField(null=True, default=True)
    CreatedDate = models.DateTimeField(default=timezone.now)
    CreatedBy = models.CharField(max_length=50,default="admin")
    ModifiedBy = models.CharField(max_length=50,default="admin")
    ModifiedDate = models.DateTimeField(default=timezone.now)
    Email = models.CharField(max_length=100,default="")
    MobileNo = models.CharField(max_length=12,default="")

    def save(self, *args, **kwargs):
        self.Password = make_password(self.Password)
        self.ConfirmPassword = make_password(self.ConfirmPassword)
        super(UserRegistration, self).save(*args, **kwargs)

    def __str__(self):

        return str(self.Id)



class Departments(models.Model):
    Id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(UserRegistration, on_delete=models.CASCADE,null=False)
    DepartmentName = models.CharField(max_length=100)

    def __str__(self):

        return str(self.Id)


class Employee(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=False)
    UserId = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, null=False)
    DepartmentId = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
    MobileNo = models.CharField(max_length=12, null=False)
    EmailId = models.CharField(max_length=100, null=False)
    Address = models.CharField(max_length=200)


class Visitors(models.Model):
    Id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, null=False)
    Name = models.CharField(max_length=100, null=False)
    MobileNo = models.CharField(max_length=12, null=False)
    Email = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    EmployeeId = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    Pic = models.CharField(max_length=200)
    IdType = models.CharField(max_length=50)
    IdNumber = models.CharField(max_length=20)
    IdPic = models.CharField(max_length=200)
    InTime = models.TimeField()
    OutTime = models.TimeField()
