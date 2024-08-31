from django.http import JsonResponse
from playground.models import MovieTypes
from playground.serializers import MovieTypesSerializer
from rest_framework.parsers import JSONParser
from django.core.exceptions import ObjectDoesNotExist


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
