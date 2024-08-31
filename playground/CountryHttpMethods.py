from django.http import JsonResponse
from playground.models import Country
from playground.serializers import CountrySerializer
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


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