from django.contrib import admin
from .models import UserRegistration, Departments, Employee, Visitors
admin.site.register(UserRegistration)
admin.site.register(Departments)
admin.site.register(Employee)
admin.site.register(Visitors)
