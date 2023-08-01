from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm

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
    form=EmployeeForm()
    context={
        'form':form,
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