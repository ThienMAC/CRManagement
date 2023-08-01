from django.forms import ModelForm,widgets
from .models import Employee,User
from django import forms
import datetime


class EmployeeForm(ModelForm):
    
    class Meta:
        model=Employee
        fields=["emp_Firstname","emp_Lastname","emp_Dob","emp_Gender"]
        