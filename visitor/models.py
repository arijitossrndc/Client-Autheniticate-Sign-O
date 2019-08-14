from django.db import models


class UserRegistration(models.Model):
    Id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50, null=False)
    Password = models.CharField(max_length=100, null=False)
    Name = models.CharField(max_length=50, null=False)
    Salt = models.CharField(max_length=20, null=False)
    isDeleted = models.BooleanField(null=False, default=False)
    StartDate = models.DateTimeField(null=False)
    ExpiredDate = models.DateTimeField(null=False)
    Amount = models.DecimalField(null=False, max_digits=10000000, decimal_places=4)
    EmailService = models.BooleanField(null=False, default=True)
    CreatedDate = models.DateTimeField()
    CreatedBy = models.CharField(max_length=50)
    ModifiedBy = models.CharField(max_length=50)
    ModifiedDate = models.DateTimeField()
    Email = models.CharField(max_length=100)
    MobileNo = models.CharField(max_length=12)


class Departments(models.Model):
    Id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(UserRegistration, on_delete=models.CASCADE,null=False)
    DepartmentName = models.CharField(max_length=100)


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
