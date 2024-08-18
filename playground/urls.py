from django.urls import path
from playground import views
from django.urls import include, re_path

urlpatterns = [
    
    # re_path(r'^department$',views.departmentApi),
    # re_path(r'^department/([0-9]+)$',views.departmentApi),
    
    # re_path(r'^employee$',views.employeeApi),
    # re_path(r'^employee/([0-9]+)$',views.employeeApi)
    
    re_path(r'^netflix$',views.NetflixApi),
    re_path(r'^netflix/(s[0-9]+)$',views.NetflixApi),
    
    re_path(r'^trigger-error/',views.trigger_error)
]
