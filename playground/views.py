from venv import logger
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging
from .validations import is_valid_country,is_valid_movietype
from .NetflixHTTPMethods import *
from .CountryHttpMethods import *
from .MovieTypesHttpMethods import *

def say_hello(request):
    return render(request, 'hello.html', {'name':'Mosh'})
  

def trigger_error(request):
    raise ValueError("This is a test exception.")

@csrf_exempt
def NetflixApi(request, id=None):
    if request.method == 'GET':
        if id:
            return get_netflix_by_id(id) 
        else:
            return get_netflix()
    
    elif request.method == 'POST':
        return post_netflix(request)
    
    elif request.method == 'PUT':
        return put_netflix(request, id)
    
    elif request.method == 'PATCH':
        return patch_netflix(request, id)
    
    elif request.method == 'DELETE':
        return delete_netflix(request, id)

@csrf_exempt
def CountryApi(request, id=None):
    if request.method == 'GET':
        if id:
            return get_with_id_Country(id) 
        else:
            return get_Country()
    
    elif request.method == 'POST':
        return post_Country(request)

    elif request.method == 'PUT':
        return put_Country(request, id)
    
    elif request.method == 'DELETE':
        return delete_Country(request, id)
    
    
@csrf_exempt
def MovieTypeApi(request, id=None):
    if request.method == 'GET':
        if id:
            return get_with_id_MovieTypes(id) 
        else:
            return get_MovieTypes()
    
    elif request.method == 'POST':
        return post_MovieType(request)
    
    elif request.method == 'PUT':
        return put_MovieType(request, id)
    
    elif request.method == 'DELETE':
        return delete_MovieType(request, id)
    

