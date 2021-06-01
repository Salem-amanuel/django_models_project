from django.db import models
from datetime import datetime 
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 400)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.dept_name

class Certificate_type(models.Model):
    Certificate_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Certificate_type
    
class Grade(models.Model):
    grade = models.CharField(max_length=1)
    
    def __str__(self):
        return self.grade 
    
class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length = 50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    year_of_graduation = models.IntegerField()
    Certificate_type = models.ForeignKey(Certificate_type, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name 


      
    


