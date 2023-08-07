from django.urls import path
from . import views

urlpatterns = [
    path("employeeList",views.employeeList,name="employeeList"),
    path("userList",views.userList,name="userList"),
    path("addEmployee",views.addEmployee,name="addEmployee"),
    path("employeeDetail/<int:id>",views.employeeDetail,name="employeeDetail"),
    path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),
]
