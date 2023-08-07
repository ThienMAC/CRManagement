from django.shortcuts import render, redirect, get_object_or_404
from HRManagement.models import User, Employee
from HRManagement.views import employeeList
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
#Login -- url: ""
def login(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        try:
            user = get_object_or_404(User,us_username=username, us_password=password)
            if user is not None:
                return employeeList(request)
        except:
            msg = 'The username or password is incorrect'
            return render(request, 'login/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form': form})