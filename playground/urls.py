from django.urls import path
from playground import views
from django.urls import include, re_path
from .views import get_netflix, post_netflix, put_netflix, patch_netflix, delete_netflix,get_netflix_by_id

urlpatterns = [
    
    
    re_path(r'^netflix/$', get_netflix, name='get_netflix'),
    re_path(r'^netflix/(?P<id>s[0-9]+)/$', get_netflix_by_id, name='get_netflix_by_id'),  
    re_path(r'^netflix/add/$', post_netflix, name='post_netflix'),
    
    re_path(r'^netflix/update/(?P<id>s[0-9]+)/$', put_netflix, name='put_netflix'),
    re_path(r'^netflix/patch/(?P<id>s[0-9]+)/$', patch_netflix, name='patch_netflix'),
    re_path(r'^netflix/delete/(?P<id>s[0-9]+)/$', delete_netflix, name='delete_netflix'),

    
]
