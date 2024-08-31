from django.db import models


# class Departments(models.Model):
#     DepartmentId = models.AutoField(primary_key=True)
#     DepartmentName = models.CharField(max_length=500)
#     DepartmentNumber = models.IntegerField()
    
    
# class Employees(models.Model):
#     EmployeeId = models.AutoField(primary_key=True)
#     EmployeeName = models.CharField(max_length=500)    
#     Department = models.CharField(max_length=500)    
#     DateOfJoining = models.DateField()
#     PhotoFileName = models.CharField(max_length=500)
    


class Netflix(models.Model):
    show_id = models.CharField(primary_key=True,max_length=50)
    type = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=200)
    cast_members = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_added = models.DateField()
    release_year = models.IntegerField()
    rating = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    listed_in = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
      
class MovieTypes(models.Model):
    TID = models.AutoField(primary_key=True)
    TypesOfMovies = models.CharField(max_length=20)
    
class Country(models.Model):
    CID = models.AutoField(primary_key=True)
    Country = models.CharField(max_length=20)    
          