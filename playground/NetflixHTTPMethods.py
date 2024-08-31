from django.http import JsonResponse
from playground.models import Netflix
from playground.serializers import NetflixSerializer
import logging
from .validations import is_valid_country,is_valid_movietype
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


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
    mt_name = net_data.get('type', '')

    errors = {}

    # Validate country
    if not is_valid_country(country_name):
        errors["country"] = [f"Country '{country_name}' is not a valid country."]

    # Validate movie type
    if not is_valid_movietype(mt_name):
        errors["type"] = [f"Type of Movie '{mt_name}' is not a valid Movie Type."]

    net_serializer = NetflixSerializer(data=net_data)
    
    # Check serializer errors
    if not net_serializer.is_valid():
        errors.update(net_serializer.errors)

    if errors:
        return JsonResponse({
            "message": "Validation failed",
            "results": [],
            "errors": errors
        }, status=400)

    net_serializer.save()
    return JsonResponse({
        "message": "Added successfully",
        "results": [net_serializer.data]
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
    net_serializer = NetflixSerializer(net, data=net_data, partial=True)

    errors = {}

    # Validate country if it's being updated
    if country_name and not is_valid_country(country_name):
        errors["country"] = [f"Country '{country_name}' is not a valid country."]

    # Validate movie type if it's being updated
    if mt_name and not is_valid_movietype(mt_name):
        errors["type"] = [f"Type of Movie '{mt_name}' is not a valid Movie Type."]

    # Check serializer errors
    if not net_serializer.is_valid():
        errors.update(net_serializer.errors)

    if errors:
        return JsonResponse({
            "message": "Validation failed",
            "results": [],
            "errors": errors
        }, status=400)

    net_serializer.save()
    return JsonResponse({
        "message": "Updated successfully",
        "results": [net_serializer.data]
    }, safe=False)


def patch_netflix(request, id):
    try:
        net = Netflix.objects.get(show_id=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)
    
    net_data = JSONParser().parse(request)

    if len(net_data) != 1:
        return JsonResponse({
            "message": "Only one field can be updated at a time.",
            "results": []
        }, status=400)
    
    field_to_update = list(net_data.keys())[0]
    field_value = net_data[field_to_update]
    errors = {}

    # Validate the field being updated
    if field_to_update == 'country' and not is_valid_country(field_value):
        errors["country"] = [f"Country '{field_value}' is not a valid country."]
    elif field_to_update == 'type' and not is_valid_movietype(field_value):
        errors["type"] = [f"Type of Movie '{field_value}' is not a valid Movie Type."]

    if errors:
        return JsonResponse({
            "message": "Validation failed",
            "results": [],
            "errors": errors
        }, status=400)
    
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