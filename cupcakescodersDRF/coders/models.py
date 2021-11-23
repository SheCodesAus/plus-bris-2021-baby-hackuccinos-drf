from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum
from datetime import date

# Create your models here.
class coders(models.Model):
    date_created = models.DateField(default=date.today) 
    student_ID = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='student_ID_coders'
    )
    image = models.URLField()    
    current_role = models.TextField()
    tech_industry = models.BooleanField() 
    programs_complete = models.CharField(max_length=200)
    programs_interested = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    mentoring = models.CharField(max_length=200)
    partner_hire = models.BooleanField() 
    post_study = models.BooleanField() 