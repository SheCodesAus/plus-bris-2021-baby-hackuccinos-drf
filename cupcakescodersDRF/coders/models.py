from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum
from datetime import date

# Create your models here.
class coders(models.Model):
    student_ID = models.TextField()
    date_created = models.DateField(default=date.today) 
    image = models.URLField()    
    current_role = models.TextField()
    tech_industry = models.BooleanField() 
    programs_complete = models.CharField(max_length=200)
    programs_interested = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    mentoring = models.CharField(max_length=200)
    partner_hire = models.CharField(max_length=200)
    post_study = models.BooleanField() 
