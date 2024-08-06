from django.urls import path
from playground import views

urlpatterns = [
    
    url(r'^department$',views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi)
]
