from venv import logger
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from playground.models import Netflix
from playground.serializers import NetflixSerializer

def say_hello(request):
    return render(request, 'hello.html', {'name':'Mosh'})
  

def trigger_error(request):
    raise ValueError("This is a test exception.")

# @csrf_exempt
# def departmentApi(request,id=0):
#     if request.method == 'GET':
#         departments = Departments.objects.all()
#         departments_serializer=DepartmentSerializer(departments,many=True)
#         return JsonResponse({
#             "message": f"Fetched {departments.count()} records successfully",
#             "results": departments_serializer.data
#          }, safe=False)
#     elif request.method == 'POST':
#         departments_data=JSONParser().parse(request)
#         departments_serializer=DepartmentSerializer(data=departments_data)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse({
#                 "message": "Added successfully",
#                 "results": [departments_serializer.data]
#             }, safe=False)
#         return JsonResponse({
#             "message": "Failed to add",
#             "results": []
#         }, safe=False)
#     elif request.method == 'PUT':
#         departments_data=JSONParser().parse(request)
#         departments=Departments.objects.get(DepartmentId=departments_data['DepartmentId'])
#         departments_serializer=DepartmentSerializer(departments,data=departments_data)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse({
#                 "message": "Updated successfully",
#                 "results": [departments_serializer.data]
#             }, safe=False)
#         return JsonResponse({
#             "message": "Failed to update",
#             "results": []
#         }, safe=False)
#     elif request.method == 'PATCH':
#         departments_data = JSONParser().parse(request)
#         department = Departments.objects.get(DepartmentId=id)
#         departments_serializer = DepartmentSerializer(department, data=departments_data, partial=True)
#         if departments_serializer.is_valid():
#             departments_serializer.save()
#             return JsonResponse({
#                 "message": "Field updated successfully",
#                 "results": [departments_serializer.data]
#             }, safe=False)
#         return JsonResponse({
#             "message": "Failed to update field",
#             "results": []
#         }, safe=False)
#     elif request.method == 'DELETE':
#         departments=Departments.objects.get(DepartmentsId=id)
#         Departments.delete()
#         return JsonResponse("Deleted Successfully", safe=False)
    
  
    
    
# @csrf_exempt
# def employeeApi(request,id=0):
#     if request.method == 'GET':
#         employees = Employees.objects.all()
#         employees_serializer=EmployeeSerializer(employees,many=True)
#         return JsonResponse({
#             "message": f"Fetched {employees.count()} records successfully",
#             "results": employees_serializer.data
#          }, safe=False)
#     elif request.method == 'POST':
#         employees_data=JSONParser().parse(request)
#         employees_serializer=EmployeeSerializer(data=employees_data)
#         if employees_serializer.is_valid():
#             employees_serializer.save()
#             return JsonResponse({
#                 "message": "Added successfully",
#                 "results": [employees_serializer.data]
#             }, safe=False)
#         return JsonResponse({
#             "message": "Failed to add",
#             "results": []
#         }, safe=False)
#     elif request.method == 'PUT':
#         employees_data=JSONParser().parse(request)
#         employees=Employees.objects.get(EmployeeId=employees_data['EmplyeeId'])
#         employees_serializer=EmployeeSerializer(employees,data=employees_data)
#         if employees_serializer.is_valid():
#             employees_serializer.save()
#             return JsonResponse({
#                 "message": "Field updated successfully",
#                 "results": [employees_serializer.data]
#             }, safe=False)
#         return JsonResponse({
#             "message": "Failed to update field",
#             "results": []
#         }, safe=False)
#     elif request.method == 'PATCH':
#         employees_data = JSONParser().parse(request)
#         employees = Employees.objects.get(EmployeeId=employees_data['EmplyeeId'])
#         employees_serializer = EmployeeSerializer(employees, data=employees_data, partial=True)
#         if employees_serializer.is_valid():
#             employees_serializer.save()
#             return JsonResponse({
#                 "message": "Field updated successfully",
#                 "results": [employees_serializer.data]
#             }, safe=False)
#         return JsonResponse({
#             "message": "Failed to update field",
#             "results": []
#         }, safe=False)
#     elif request.method == 'DELETE':
#         employees=Employees.objects.get(employeesID=id)
#         Employees.delete()
#         return JsonResponse("Deleted Successfully", safe=False)
   
# @csrf_exempt
# def NetflixApi(request,id=0):
#     if request.method == 'GET':
#         net = Netflix.objects.all()
#         net_serializer=NetflixSerializer(net,many=True)
#         return JsonResponse({
#             "message": f"Fetched {net.count()} records successfully",
#             "results": net_serializer.data
#          }, safe=False)
#     elif request.method == 'POST':
#         net_data = JSONParser().parse(request)
#         net_serializer = NetflixSerializer(data=net_data)
#         if net_serializer.is_valid():
#             net_serializer.save()
#             return JsonResponse({
#                 "message": "Added successfully",
#                 "results": [net_serializer.data]
#             }, safe=False) 
#         return JsonResponse({
#             "message": "Failed to add",
#             "results": [],
#             "errors": net_serializer.errors  
#         }, safe=False)

#     elif request.method == 'PUT':
#         net_data = JSONParser().parse(request)
#         net = Netflix.objects.get(show_id=net_data["show_id"])
#         net_serializer = NetflixSerializer(net, data=net_data)
#         if net_serializer.is_valid():
#             net_serializer.save()
#             return JsonResponse({
#                 "message": "Field updated successfully",
#                 "results": [net_serializer.data]
#             }, safe=False)
#         return JsonResponse({
#             "message": "Failed to update field",
#             "results": [],
#             "errors": net_serializer.errors  
#         }, safe=False)

#     elif request.method == 'PATCH':
#         net_data = JSONParser().parse(request)
#         net = Netflix.objects.get(show_id=net_data['show_id'])
#         net_serializer = NetflixSerializer(net, data=net_data, partial=True)
#         if net_serializer.is_valid():
#             net_serializer.save()
#             return JsonResponse({
#                 "message": "Field updated successfully",
#                 "results": [net_serializer.data]
#             }, safe=False)
#         return JsonResponse({
#             "message": "Failed to update field",
#             "results": [],
#             "errors": net_serializer.errors  
#         }, safe=False)

#     elif request.method == 'DELETE':
#         net = Netflix.objects.get(show_id=id)
#         net.delete()
#         return JsonResponse({
#             "message": "Deleted Successfully"
#         }, safe=False)


@csrf_exempt
@csrf_exempt
def get_netflix_by_id(request, id):
    try:
        # Log the ID being fetched
        logger.info(f"Fetching Netflix record with ID: {id}")
        
        # Fetch the Netflix record using the ID
        net = Netflix.objects.get(show_id=id)
        
        # Serialize the fetched data
        net_serializer = NetflixSerializer(net)
        
        # Return the serialized data in the specified JSON format
        return JsonResponse({
            "message": "Fetched record successfully",
            "results": [net_serializer.data]
        }, safe=False)
    
    except ObjectDoesNotExist:
        # Log and return a 404 response if the record is not found
        logger.warning(f"Netflix record with ID {id} not found.")
        return JsonResponse({
            "message": f"Netflix record with ID {id} not found."
        }, status=404)


@csrf_exempt
def get_netflix(request):
    net = Netflix.objects.all()
    net_serializer = NetflixSerializer(net, many=True)
    return JsonResponse({
        "message": f"Fetched {net.count()} records successfully",
        "results": net_serializer.data
    }, safe=False)

@csrf_exempt
def post_netflix(request):
    net_data = JSONParser().parse(request)
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

@csrf_exempt
def put_netflix(request, id):
    if request.method == 'PUT':
        try:
            net = Netflix.objects.get(show_id=id)
        except ObjectDoesNotExist:
            return JsonResponse({
                "message": f"Netflix record with ID {id} not found."
            }, status=404)

        net_data = JSONParser().parse(request)
        net_serializer = NetflixSerializer(net, data=net_data)
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
    else:
        return JsonResponse({
            "message": "Invalid request method"
        }, status=405)

@csrf_exempt
def patch_netflix(request, id):
    try:
        net = Netflix.objects.get(show_id=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": "Resource not found"
        }, status=404)
    
    net_data = JSONParser().parse(request)
    net_serializer = NetflixSerializer(net, data=net_data, partial=True)
    if net_serializer.is_valid():
        net_serializer.save()
        return JsonResponse({
            "message": "Field updated successfully",
            "results": [net_serializer.data]
        }, safe=False)
    return JsonResponse({
        "message": "Failed to update field",
        "results": [],
        "errors": net_serializer.errors
    }, safe=False)

@csrf_exempt
def delete_netflix(request, id):
    try:
        net = Netflix.objects.get(show_id=id)
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": "Resource not found"
        }, status=404)
    
    net.delete()
    return JsonResponse({
        "message": "Deleted Successfully"
    }, safe=False)