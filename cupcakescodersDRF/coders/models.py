from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum
from datetime import date

# Create your models here.
class coders(models.Model):
    student_ID = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='UPDATEREQUIREDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'
    )
    first_name = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='UPDATEREQUIREDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'
    )        
    last_name = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='UPDATEREQUIREDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'
    )
    email = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='UPDATEREQUIREDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'
    )    
    date_created = models.DateField(default=date.today) 
    image = models.URLField()    
    current_role = models.TextField()
    tech_industry = models.BooleanField() 
    PROGRAMS = (
        ('1 Day Tech Workshop','1 Day Tech Workshop'),
        ('1 Week Flash Program','1 Week Flash Program'),
        ('She Codes Plus Program','She Codes Plus Program')
    )
    programs_complete = models.CharField(max_length=200, choices=PROGRAMS)
    programs_interested = models.CharField(max_length=200, choices=PROGRAMS)
    LOCATIONS = (
        ('Brisbane','Brisbane'),
        ('Perth','Perth'),
        ('Port Hedland','Port Hedland')        
    )
    location = models.CharField(max_length=200, choices=LOCATIONS)
    MENTOR = (
        ('Yes','Yes'),
        ('No','No'),
        ('No, But Intested','No, But Interested')            
    )
    mentoring = models.CharField(max_length=200, choices=MENTOR)
    PARTNERS = (
        ('BHP','BHP'),
        ('Bunnings','Bunnings'),
        ('VGW','VGW')            
    )
    partner_hire = models.CharField(max_length=200, choices=PARTNERS)
    post_study = models.BooleanField() 
