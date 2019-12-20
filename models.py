from django.db import models
from django.conf import settings
from django.utils import timezone

class Student(models.Model):
    name=models.CharField(max_length=100)
    regNo=models.CharField(max_length=100,primary_key=True)
    classs=models.CharField(max_length=100)
    class Meta:
        db_table = 'stud'

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    empId=models.CharField(max_length=100)
    sub=models.CharField(max_length=100)
    class Meta:
        db_table = 'stud'

# Create your models here.
