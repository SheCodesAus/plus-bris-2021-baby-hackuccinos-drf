from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

# Create your models here.
class CustomUser(AbstractUser):
    student_id = models.CharField(max_length=100)
    date_created = models.DateField(default=date.today)    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    pass
    def __str__(self):
        #display as just the username (no {})
        return self.username