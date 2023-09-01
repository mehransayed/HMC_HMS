from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def Home(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'Home.html')


def Division(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'Division.html')

def Employee(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'EmployeeRegistration.html')

def Department(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'Department.html')

def Designation(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'Designation.html')


def Grade(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'Grade.html')
