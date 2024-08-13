from rest_framework import serializers
from playground.models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Departments
        fields = ('DepartmentId','DepartmentName','DepartmentNumber')
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employees
        fields = ('EmployeeId','EmployeeName','Department', 'DateOfJoining','PhotoFileName')        