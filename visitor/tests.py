from django.db import models
from .models import UserRegistration
b = UserRegistration.objects.getall()
print(b)
