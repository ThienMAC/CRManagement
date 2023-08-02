from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_Firstname=models.CharField(max_length=200)
    emp_Lastname=models.CharField(max_length=500)
    emp_Dob=models.DateField()
    emp_Gender=models.BooleanField(default=0)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.IntegerField(default=0)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.emp_Firstname} {self.emp_Lastname}"
    

class User(models.Model):
    us_username=models.CharField(max_length=50)
    us_password=models.CharField(max_length=50)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.IntegerField(default=0)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.IntegerField(default=0)

    def __str__(self):
        return self.us_username