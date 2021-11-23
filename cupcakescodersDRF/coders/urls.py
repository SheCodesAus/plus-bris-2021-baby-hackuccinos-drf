from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
     path('coders/', views.CodersList.as_view()),
     path('coders/<int:pk>/', views.CodersDetail.as_view()),
     # path('coders/enrolments/', views.enrolments)
     path('coders/enrolments/', views.Enrolments.as_view()),
     path('coders/partnerjobs/', views.PartnersJobs.as_view()),
     path('coders/techjobs/', views.TechJobs.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)