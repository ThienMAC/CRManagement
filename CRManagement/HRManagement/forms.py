from django.forms import ModelForm,widgets
from .models import Employee,User
from django import forms
import datetime


class EmployeeForm(ModelForm):
    emp_Firstname=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "placeholder":"Enter your first name"
    }))
    emp_Lastname=forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "placeholder":"Enter your last name"
    }))
    emp_Dob=forms.DateField(widget=forms.DateInput(
        attrs={             
            'type': 'date',
    }))
    emp_Gender=forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'type':'checkbox'
        }
    ))
    class Meta:
        model=Employee
        fields=["emp_Firstname","emp_Lastname","emp_Dob","emp_Gender"]
        