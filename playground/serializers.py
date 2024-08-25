from rest_framework import serializers
from playground.models import Netflix

# class DepartmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Departments
#         fields = ('DepartmentId','DepartmentName','DepartmentNumber')
        
# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Employees
#         fields = ('EmployeeId','EmployeeName','Department', 'DateOfJoining','PhotoFileName')        
        
class NetflixSerializer(serializers.ModelSerializer):
    class Meta:
        model= Netflix
        fields =('show_id', 'type', 'title', 'director', 'cast_members', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description')
        
                  