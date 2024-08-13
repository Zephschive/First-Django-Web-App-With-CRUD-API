from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from playground.models import Departments, Employees
from playground.serializers import DepartmentSerializer, EmployeeSerializer

def say_hello(request):
    return render(request, 'hello.html', {'name':'Mosh'})


@csrf_exempt
def departmentApi(request,id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer=DepartmentSerializer(departments,many=True)
        return JsonResponse({
            "message": f"Fetched {departments.count()} records successfully",
            "results": departments_serializer.data
         }, safe=False)
    elif request.method == 'POST':
        departments_data=JSONParser().parse(request)
        departments_serializer=DepartmentSerializer(data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse({
                "message": "Added successfully",
                "results": [departments_serializer.data]
            }, safe=False)
        return JsonResponse({
            "message": "Failed to add",
            "results": []
        }, safe=False)
    elif request.method == 'PUT':
        departments_data=JSONParser().parse(request)
        departments=Departments.objects.get(DepartmentId=departments_data['DepartmentId'])
        departments_serializer=DepartmentSerializer(departments,data=departments_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'PATCH':
        departments_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=id)
        departments_serializer = DepartmentSerializer(department, data=departments_data, partial=True)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Field Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Field", safe=False)
    elif request.method == 'DELETE':
        departments=Departments.objects.get(DepartmentsId=id)
        Departments.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
  
    
    
@csrf_exempt
def employeeApi(request,id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employees_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        employees_data=JSONParser().parse(request)
        employees=Employees.objects.get(EmployeeId=employees_data['EmplyeeId'])
        employees_serializer=EmployeeSerializer(employees,data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'PATCH':
        employees_data = JSONParser().parse(request)
        employees = Employees.objects.get(EmployeeId=employees_data['EmplyeeId'])
        employees_serializer = EmployeeSerializer(employees, data=employees_data, partial=True)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Field Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Field", safe=False)
   
    