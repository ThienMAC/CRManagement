from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Employee,User

# Create your views here.
#Login -- url: ""
def login(request):

    context={

    }
    return render(request,"HRManagement/login.html",context)


# Get all Employees -- url: .../employeeList
def employeeList(request):

    employees=Employee.objects.all()

    context={
        'employees':employees
    }

    return render(request,"HRManagement/employeeList.html",context)

# Get all users -- url: .../userList
def userList(request):

    users=User.objects.all()

    context={
        'users':users
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
        us_created_by=0
        us_modified_by=0
        user=User(
            us_username=us_username,
            us_password=us_password,
            employee=emp_saved,
            created_by=us_created_by,
            modified_by=us_modified_by
        )
        user.save()
    context={
        
    }

    return render(request,"HRManagement/addEmployee.html",context)

# View Employee and user for that employee -- url: .../employeeDetail
def employeeDetail(request, id):

    employee=Employee.objects.get(id=id)
    if employee is None:
        return
    user=User.objects.get(employee=employee)
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
        
        employee.emp_Firstname=emp_Firstname
        employee.emp_Lastname=emp_Lastname
        employee.emp_Dob=emp_Dob
        employee.emp_Gender=emp_Gender
        employee.created_by=created_by
        employee.modified_by=modified_by
        
        
        employee.save()

        us_username=request.POST.get("us_username")
        us_password=request.POST.get("us_password")
        us_created_by=0
        us_modified_by=0


        user.us_username=us_username
        user.us_password=us_password
        user.employee=employee
        user.created_by=us_created_by
        user.modified_by=us_modified_by
        user.save()

        return redirect("/hrmanagement/employeeList")

    context={
        'employee':employee,
        'user':user
    }


    return render(request,"HRManagement/employeeDetail.html",context)

   

# Delete Employee and user for that employee -- url: ../deleteEmployee
def deleteEmployee(request,id):

    employee=Employee.objects.get(id=id)
    if employee is None:
        return    
    user=User.objects.get(employee=employee)
    if user is None:
        return
    print(employee)
    print(user)
    context={
        'employee':employee,
        'user':user
    }

    if request.method=='POST':
        print(employee)
        print(user)
        user.delete()
        employee.delete()
        return redirect("/hrmanagement/employeeList")
    
    

    return render(request,'HRManagement/deleteEmployee.html',context)

    