

from django.contrib import admin
from django.urls import path
from HR import views

urlpatterns = [
    path('HR', views.Home, name='Home'),
    
    #Employee URLS
    path('Employee', views.Employee, name='Employee'),
    path('EmployeeReg', views.EmpReg, name='EmpReg'),
    

    #Staff Category URLS
    path('Division', views.Division, name='Division'),
    path('DivisionReg', views.DivisionRegistration, name='DivisionRegistration'),
    
    
    path('Department', views.Department, name='Department'),
    path('DepartmentReg', views.DepartmentRegistration, name='DepartmentRegistration'),
    path('edit_department/<int:id_dep>', views.edit_department, name ='edit_department'),
    path('update_department/<int:id_dep>', views.update_department, name ='update_department'),


    path('Designation', views.Designation, name='Designation'),
    path('DesignationReg', views.DesignationRegistration, name='DesignationRegistration'),
    path('edit_designation/<int:id_des>', views.edit_designation, name ='edit_designation'),
    path('update_designation/<int:id_des>', views.update_designation, name ='update_designation'),

    path('Location', views.Location, name='Location'),
    path('LocationReg', views.LocationRegistration, name='LocationRegistration'),
    path('edit_location/<int:id>', views.edit_location, name ='edit_location'),
    path('update_location/<int:id>', views.update_location, name ='update_location'),

    path('EmployeeType', views.EmployeeType, name='EmployeeType'),
    path('EmployeeTypeReg', views.EmployeeTypeRegistration, name='EmployeeTypeRegistration'),


    path('EmployementType', views.EmployeementType, name='EmployeementType'),
    path('EmployementTypeReg', views.EmployeementTypeRegistration, name='EmployeementTypeRegistration'),

    path('Grade', views.Grade, name='Grade')
]
