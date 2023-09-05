from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from HR.models import DivisionModel
from django.contrib import messages


# import required modules
import MySQLdb
  
# connect python with mysql with your hostname, 
# username, password and database
db= MySQLdb.connect("localhost", "root", "test", "HMC_HMS")

# Create your views here.
def Home(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'Home.html')


def Division(request):
        #cursor= db.cursor()
        ## execute your query
        #cursor.execute("SELECT * FROM Division")
        
        ## fetch all the matching rows 
        #result = cursor.fetchall()
        #messages.success(request, result)
        #return HttpResponse(result)
        return render(request, "Division.html")


def DivReg(request):
    #if request.method=="POST":
    #    if request.POST.get('Name'):
    #        saverecord = DivisionModel()
    #        saverecord.Name = request.POST.get('Name')
    #        saverecord.save()
    #        return render(request, "Division.html")
    #    else:
    #        return render(request,"DivisionRegistration.html")
    #else:
        return render(request, 'DivisionAdd.html')   


def Employee(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'Employee.html')

def EmpReg(request):
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