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
        Departments = Departments.objects.all()
        Departments_serializer=DepartmentSerializer(Departments,many=True)
        return JsonResponse(Departments_serializer.data, safe=False)
    elif request.method == 'POST':
        Departments_data=JSONParser().parse(request)
        Departments_serializer=DepartmentSerializer(data=Departments_data)
        if Departments_serializer.is_valid():
            Departments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        Departments_data=JSONParser().parse(request)
        Departments=Departments.objects.get(DepartmentId=Departments_data['DepartmentId'])
        Departments_serializer=DepartmentSerializer(Departments,data=Departments_data)
        if Departments_serializer.is_valid():
            Departments_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        Departments=Departments.objects.get(DepartmentsId=id)
        Departments.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    