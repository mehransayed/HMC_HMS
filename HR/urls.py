

from django.contrib import admin
from django.urls import path
from HR import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Division', views.Division, name='Division'),
    path('Employee', views.Employee, name='Employee'),
    path('Department', views.Department, name='Department'),
    path('Designation', views.Designation, name='Designation'),
    path('Grade', views.Grade, name='Grade')
]
