from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee,User

# Create your views here.
# Get all Employees -- url: .../employeeList
def employeeList(request):
    context={

    }

    return render(request,"HRManagement/employeeList.html",context)

# Get all users -- url: .../userList
def userList(request):
    context={

    }

    return render(request,"HRManagement/userList.html",context)

# Add Employee and Users for that employee -- url: .../addEmployee
def addEmployee(request):
    if request.method=="POST":
        emp_Firstname=request.POST.get("emp_Firstname")
        emp_Lastname=request.POST.get("emp_Lastname")
        emp_Dob=request.POST.get("emp_Dob")
        sex=request.POST.get("gender_male")
        if sex == "male":
            emp_Gender=True
        else:
            emp_Gender=False
        created_by=0
        modified_by=0
        emp=Employee(
            emp_Firstname=emp_Firstname,
            emp_Lastname=emp_Lastname,
            emp_Dob=emp_Dob,
            emp_Gender=emp_Gender,
            created_by=created_by,
            modified_by=modified_by
        )
        
        emp.save()
        
        emp_saved=Employee.objects.get(pk=emp.id)
        us_username=request.POST.get("us_username")
        us_password=request.POST.get("us_password")
        emp_id=emp_saved.id
        us_created_by=0
        us_modified_by=0
        user=User(
            us_username=us_username,
            us_password=us_password,
            emp_id=emp_id,
            created_by=us_created_by,
            modified_by=us_modified_by
        )
        user.save()
    context={
        
    }

    return render(request,"HRManagement/addEmployee.html",context)

# View Employee and user for that employee -- url: .../employeeDetail
def employeeDetail(request, id):
    return HttpResponse("This is employeeDetail for "+id)

# Update Employee and user for that employee -- url: .../updateEmployee
def updateEmployee(request, id):
    return HttpResponse("This is updateEmployee for "+id)

# Delete Employee and user for that employee -- url: ../deleteEmployee
def deleteEmployee(request,id):
    return HttpResponse("This is deleteEmployee for "+id)