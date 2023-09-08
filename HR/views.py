from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

from .models import DepartmentInsert, DesignationInsert, LocationInsert, EmployeeRegModel
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
        return render(request, "Division.html")


def DivisionRegistration(request):
    if request.method=="POST":
        if request.post.get('name'):
            #saverecord = divisionmodel()
            #saverecord.name = request.post.get('name')
            #saverecord.save()
            return render(request, "Division.html")
        else:
            return render(request,"DivisionRegistration.html")
    else:
        return render(request, 'DivisionAdd.html')   


def Employee(request):
    try:
        EmployeeList = EmployeeRegModel.objects.all()
        return render(request, 'Employee.html', {'EmployeeList': EmployeeList})
    except:
        return render(request, 'Employee.html')

def EmpReg(request):
    if request.method=="POST":
        if request.POST.get('Stafftype'):
            saverecord = EmployeeRegModel()
            saverecord.Staff_Type = request.POST.get('Stafftype')
            saverecord.Employment_type_id  = request.POST.get('EmployementType')
            saverecord.Employee_Title =  request.POST.get('EmployeeNameTitle')
            saverecord.Employee_name = request.POST.get('EmployeeName')
            saverecord.User_Name =  request.POST.get('UserName')
            saverecord.Father_Husb_Title = request.POST.get('FatherHusbandNameTitle')
            saverecord.Father_Husb_name = request.POST.get('FatherHusbandName')
            saverecord.Mother_name =  request.POST.get('MotherName')
            saverecord.Employee_cnic  =  request.POST.get('EmployeeCNIC')
            saverecord.Father_cnic  =  request.POST.get('FatherHusbandCNIC')
            saverecord.Contact =  request.POST.get('ContactNo')
            saverecord.Other_contact =  request.POST.get('OtherConatctNo')
            saverecord.Gender =  request.POST.get('Gender')
            saverecord.Joining_date  =  datetime.now()
            saverecord.Staff_cat_id  =  request.POST.get('StaffCategory')
            saverecord.Employee_type_id =  request.POST.get('EmployeeType')
            saverecord.Department_id =  request.POST.get('Department')
            saverecord.Location_id =  request.POST.get('Location')
            saverecord.Designation_id =  request.POST.get('Designation')
            saverecord.Salary_Grade_id =  request.POST.get('SalaryGrade')
            saverecord.Report_Direct =  request.POST.get('ReportDirect')
            saverecord.Report_InDirect =  request.POST.get('ReportIn-Direct')
            saverecord.Dept_name =  request.POST.get('Dept_name')
            saverecord.Create_by = 'Mansoor' 
            saverecord.Create_date =  datetime.now()
            saverecord.Updated_by = 'Mansoor'  
            saverecord.Updated_date = datetime.now() 
            saverecord.IsActive = True  
            saverecord.Pc_name =  'Mansoor'
            
            saverecord.save()
            EmployeeList = EmployeeRegModel.objects.all()
            return render(request, "Employee.html", {'EmployeeList': EmployeeList})
        else:
            return render(request,"EmployeeRegistration.html")
    else: 
        return render(request, 'EmployeeRegistration.html')

def Department(request):
    dept = GelDepartmentList()
    return render(request, 'Department.html', {'dept':dept})


def DepartmentRegistration(request):
    if request.method=="POST":
        if request.POST.get('Dept_name'):
            saverecord = DepartmentInsert()
            saverecord.Dept_name = request.POST.get('Dept_name')
            saverecord.create_by = 'Mehran'
            saverecord.create_date = datetime.now()
            saverecord.updated_by = 'Mehran'
            saverecord.updated_date = datetime.now()
            saverecord.pc_name = 'Mehr'
            saverecord.Is_Active = 1
            saverecord.save()

            dept = GelDepartmentList()
            return render(request, "Department.html", {'dept':dept})
        else:
            return render(request,"DepartmentAdd.html")
    else: 
        return render(request, 'DepartmentAdd.html')

def GelDepartmentList():
    dept = DepartmentInsert.objects.all()
    return dept

def edit_department(request, id_dep):
    obj_dep = DepartmentInsert.objects.get(Id=id_dep)
    context = {
        'obj_dep':obj_dep,
    }
    return render(request,"DepartmentAdd.html", context)

def update_department(request, id_dep):
    item_dep = DepartmentInsert.objects.get(Id=id_dep)
    item_dep.Dept_name = request.POST.get('Dept_name')
    item_dep.save()
    #messages.success(request, 'record Updated')
    dept = DepartmentInsert.objects.all()
    return render(request, "Department.html", {'dept':dept})




def Designation(request):
    desig = DesignationInsert.objects.all()
    return render(request, 'Designation.html', {'desig':desig})

def DesignationRegistration(request):
    if request.method=="POST":
        if request.POST.get('Designation'):
            saverecord = DesignationInsert()
            saverecord.Designation = request.POST.get('Designation')
            saverecord.create_by = 'Mehran'
            saverecord.create_date = datetime.now()
            saverecord.updatedby = 'Mehran'
            saverecord.updated_date = datetime.now()
            saverecord.pc_name = 'Mehr'
            saverecord.save()
            messages.success(request, 'record saved')

            #return redirect('/')
             
            return render(request, "DesignationAdd.html")
            #return (request,"index.html")

            #return render(request,"appemp/index.html", args)
        else:
            return render(request,"DesignationAdd.html")
    else:
        return render(request,"DesignationAdd.html")

def edit_designation(request, id_des):
    obj_des = DesignationInsert.objects.get(Id=id_des)
    context = {
        'obj_des':obj_des,
    }
    return render(request,"DesignationAdd.html", context)

def update_designation(request, id_des):
    item_d = DesignationInsert.objects.get(Id=id_des)
    item_d.Designation = request.POST.get('Designation')
    item_d.save()
    #messages.success(request, 'record Updated')
    desig = DesignationInsert.objects.all()
    return render(request, "Designation.html", {'desig':desig})


def Grade(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'Grade.html')

def Location(request):
    loc = LocationInsert.objects.all()
    return render(request, 'Location.html', {'loc':loc})

def LocationRegistration(request):
    if request.method=="POST":
        if request.POST.get('location'):
            saverecord = LocationInsert()
            saverecord.location = request.POST.get('location')
            saverecord.create_by = 'Mehran'
            saverecord.create_date = datetime.now()
            saverecord.updatedby = 'Mehran'
            saverecord.updated_date = datetime.now()
            saverecord.pc_name = 'Mehr'
            saverecord.save()
            #messages.success(request, 'record saved')

            #return redirect('/')
            item = LocationInsert.objects.get(Id=id)
            return render(request, "LocationAdd.html")
            #return (request,"index.html")

            #return render(request,"appemp/index.html", args)
        else:
            return render(request,"LocationAdd.html")
    else:
        return render(request,"LocationAdd.html")

def edit_location(request, id):
    obj = LocationInsert.objects.get(Id=id)
    context = {
        'obj':obj,
    }
    return render(request,"LocationAdd.html", context)

def update_location(request, id):
    item = LocationInsert.objects.get(Id=id)
    item.location = request.POST.get('location')
    item.save()
    #messages.success(request, 'record Updated')
    loc = LocationInsert.objects.all()
    return render(request, "Location.html", {'loc':loc})

def EmployeeType(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'EmployeeType.html')

def EmployeeTypeRegistration(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'EmployeeTypeAdd.html')

def EmployeementType(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'EmployeementType.html')

def EmployeementTypeRegistration(request):
    params = {'Name':'Mansoor', 'Place':'Hyd'}
    return render(request, 'EmployeementTypeAdd.html')