from datetime import datetime
from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class AddCourses(models.Model):
    course = models.CharField(max_length=100)
    fees = models.IntegerField()
    duration = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    

    def __str__(self):
        return self.course

class AddStudents(models.Model):
    sname = models.CharField(max_length=100)
    semail = models.EmailField(max_length=100)
    smobile = models.CharField(max_length=10)
    saddress= models.CharField(max_length=255)
    scollege = models.CharField(max_length=255)
    sdegree = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.FloatField()
    scourse= models.ForeignKey(AddCourses, on_delete=models.CASCADE)
   
    
    def __str__(self):
        return self.sname

class Notifications(models.Model):
    course = models.ForeignKey(AddCourses,on_delete=models.CASCADE)
    students = models.ForeignKey(AddStudents,on_delete=models.CASCADE)
    
    