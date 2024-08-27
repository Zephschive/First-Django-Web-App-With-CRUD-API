from django.urls import path
from playground import views
from django.urls import include, re_path


urlpatterns = [
    
   
    re_path(r'^netflix/(?P<id>s\d+)/$', views.NetflixApi),  
    re_path(r'^netflix/$', views.NetflixApi),  
]

    

