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
        

    def validate(self, data):
           if not (data.get('show_id').startswith("s")):
                    raise serializers.ValidationError("show_id should start with an s")
           elif not (data.get('type') == ['Movie','TV Show', 'News']):
                    raise serializers.ValidationError("type must be equal to either,'Movie','TV Show', 'News'")
           
                    