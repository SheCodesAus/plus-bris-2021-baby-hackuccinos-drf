from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    student_id = models.CharField(max_length=100)
    date_created = models.DateField(default=date.today)    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
