# randomizer/urls.py
from django.urls import path
from . import views

app_name = 'randomizer'

urlpatterns = [
   path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('applicants/', views.applicant_list, name='applicant_list'),
    path('run-lottery/', views.run_lottery, name='run_lottery'),
]
