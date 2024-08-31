from venv import logger
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from playground.models import Netflix,Country,MovieTypes
from playground.serializers import NetflixSerializer,CountrySerializer,MovieTypesSerializer
import logging
from .validations import is_valid_country,is_valid_movietype

def say_hello(request):
    return render(request, 'hello.html', {'name':'Mosh'})
  

def trigger_error(request):
    raise ValueError("This is a test exception.")





def get_with_id_Country(id):
    Count = Country.objects.get(CID=id)
    Count_serializer = CountrySerializer(Count)
    return JsonResponse({
        "message": f"Fetched  record with id {id} successfully",
        "results": Count_serializer.data
    }, safe=False)

def get_Country():
    Count = Country.objects.all()
    Count_serializer = CountrySerializer(Count, many=True)
    return JsonResponse({
        "message": f"Fetched {Count.count()} records successfully",
        "results": Count_serializer.data
    }, safe=False)
    
    
def post_Country(request):
    Count_data = JSONParser().parse(request)
    Count_serializer = CountrySerializer(data=Count_data)
    if Count_serializer.is_valid():
        Count_serializer.save()
        return JsonResponse({
            "message": "Added successfully",
            "results": [Count_serializer.data]
        }, safe=False)
    return JsonResponse({
        "message": "Failed to add",
        "results": [],
        "errors": Count_serializer.errors
    }, safe=False) 
    
def put_Country(request, id):
    try:
       
        Count = Country.objects.get(CID=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)
    
    COUNT_data = JSONParser().parse(request)
    Count_serializer = CountrySerializer(Count, data= COUNT_data, partial=True)
    if Count_serializer.is_valid():
        Count_serializer.save()
        return JsonResponse({
            "message": "Updated successfully",
            "results": [Count_serializer.data]
        }, safe=False)
    return JsonResponse({
        "message": "Failed to update",
        "results": [],
        "errors": Count_serializer.errors
    }, safe=False)    
    
def delete_Country(request, id):
    try:
        Count = Country.objects.get(CID=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)
    
    Count.delete()
    return JsonResponse({
        "message": "Deleted Successfully"
    }, safe=False)  

def get_with_id_MovieTypes(id):
    Movie = MovieTypes.objects.get(CID=id)
    Movie_serializer = MovieTypesSerializer(Movie)
    return JsonResponse({
        "message": f"Fetched  record with Id {id} successfully",
        "results": Movie_serializer.data
    }, safe=False)
 
    
def get_MovieTypes():
    Movie = MovieTypes.objects.all()
    Movie_serializer = MovieTypesSerializer(Movie, many=True)
    return JsonResponse({
        "message": f"Fetched {Movie.count()} records successfully",
        "results": Movie_serializer.data
    }, safe=False)
    
    
def post_MovieType(request):
    Movie_data = JSONParser().parse(request)
    Movie_serializer = MovieTypesSerializer(data=Movie_data)
    if Movie_serializer.is_valid():
        Movie_serializer.save()
        return JsonResponse({
            "message": "Added successfully",
            "results": [Movie_serializer.data]
        }, safe=False)
    return JsonResponse({
        "message": "Failed to add",
        "results": [],
        "errors": Movie_serializer.errors
    }, safe=False) 
 
def put_MovieType(request, id):
    try:
       
        MovieTP = MovieTypes.objects.get(TID=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)
    
    Movie_data = JSONParser().parse(request)
    Movie_serializer = MovieTypesSerializer(MovieTP, data=Movie_data, partial=True)
    if Movie_serializer.is_valid():
        Movie_serializer.save()
        return JsonResponse({
            "message": "Updated successfully",
            "results": [Movie_serializer.data]
        }, safe=False)
    return JsonResponse({
        "message": "Failed to update",
        "results": [],
        "errors": Movie_serializer.errors
    }, safe=False)    
        
    
def delete_MovieType(request, id):
    try:
        Movie = MovieTypes.objects.get(TID=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)
    
    Movie.delete()
    return JsonResponse({
        "message": "Deleted Successfully"
    }, safe=False)           


logger = logging.getLogger(__name__)

def get_netflix_by_id(id):
    try:
        logger.info(f"Fetching Netflix record with ID: {id}")
        net = Netflix.objects.get(show_id=id)
        net_serializer = NetflixSerializer(net)
        return JsonResponse({
            "message": "Fetched record successfully",
            "results": [net_serializer.data]
        }, safe=False)
    except ObjectDoesNotExist:
        logger.warning(f"Netflix record with ID {id} not found.")
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)

def get_netflix():
    net = Netflix.objects.all()
    net_serializer = NetflixSerializer(net, many=True)
    return JsonResponse({
        "message": f"Fetched {net.count()} records successfully",
        "results": net_serializer.data
    }, safe=False)

def post_netflix(request):
    net_data = JSONParser().parse(request)
    country_name = net_data.get('country', '')
    MT_name = net_data.get('type', '')

    # Use the validation function to check if the country is valid
    if not is_valid_country(country_name):
        return JsonResponse({
            "message": f"Country '{country_name}' is not a valid country.",
            "results": [],
            "errors": {"country": ["Invalid country."]}
        }, status=400)

    # Use the validation function to check if the MovieType is valid
    if not is_valid_country(MT_name):
        return JsonResponse({
            "message": f"Type of Movie '{MT_name}' is not a valid Movie Type.",
            "results": [],
            "errors": {"country": ["Invalid MovieType."]}
        }, status=400)
    
    net_serializer = NetflixSerializer(data=net_data)
    if net_serializer.is_valid():
        net_serializer.save()
        return JsonResponse({
            "message": "Added successfully",
            "results": [net_serializer.data]
        }, safe=False)
    return JsonResponse({
        "message": "Failed to add",
        "results": [],
        "errors": net_serializer.errors
    }, safe=False)

def put_netflix(request, id):
    try:
        net = Netflix.objects.get(show_id=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)
    
    net_data = JSONParser().parse(request)
    country_name = net_data.get('country', '')
    mt_name = net_data.get('type', '')

    # Validate country if it's being updated
    if country_name and not is_valid_country(country_name):
        return JsonResponse({
            "message": f"Country '{country_name}' is not a valid country.",
            "results": [],
            "errors": {"country": ["Invalid country."]}
        }, status=400)

    # Validate movie type if it's being updated
    if mt_name and not is_valid_movietype(mt_name):
        return JsonResponse({
            "message": f"Type of Movie '{mt_name}' is not a valid Movie Type.",
            "results": [],
            "errors": {"type": ["Invalid Movie Type."]}
        }, status=400)

    net_serializer = NetflixSerializer(net, data=net_data, partial=True)
    if net_serializer.is_valid():
        net_serializer.save()
        return JsonResponse({
            "message": "Updated successfully",
            "results": [net_serializer.data]
        }, safe=False)
    return JsonResponse({
        "message": "Failed to update",
        "results": [],
        "errors": net_serializer.errors
    }, safe=False)

def patch_netflix(request, id):
    try:
        net = Netflix.objects.get(show_id=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)
    
    net_data = JSONParser().parse(request)
    print(net_data)
   
    if len(net_data) != 1:
        return JsonResponse({
            "message": "Only one field can be updated at a time.",
            "results": []
        }, status=400)
    
    
    field_to_update = list(net_data.keys())[0]
  
    field_value = net_data[field_to_update]


    setattr(net, field_to_update, field_value)
    net.save()

    net_serializer = NetflixSerializer(net)
    return JsonResponse({
        "message": "Field updated successfully",
        "results": [net_serializer.data]
    }, safe=False)


def delete_netflix(request, id):
    try:
        net = Netflix.objects.get(show_id=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)
    
    net.delete()
    return JsonResponse({
        "message": "Deleted Successfully"
    }, safe=False)

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
    

