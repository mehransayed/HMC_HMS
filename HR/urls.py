

from django.contrib import admin
from django.urls import path
from HR import views

urlpatterns = [
    path('', views.Home, name='Home'),
    
    #Employee URLS
    path('Employee', views.Employee, name='Employee'),
    path('EmployeeReg', views.EmpReg, name='EmpReg'),
    

    #Staff Category URLS
    path('Division', views.Division, name='Division'),
    path('DivisionReg', views.DivReg, name='DivReg'),
    
    path('Department', views.Department, name='Department'),
    path('Designation', views.Designation, name='Designation'),
    path('Grade', views.Grade, name='Grade')
]
