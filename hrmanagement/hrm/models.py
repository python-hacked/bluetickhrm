from datetime import datetime
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric])
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class AddCourses(models.Model):
    course = models.CharField(max_length=100)
    fees = models.IntegerField()
    duration = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.course


class AddStudents(models.Model):
    sname = models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric])
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
    
    
class AddHr(models.Model):
    sname = models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric])
    semail = models.EmailField(max_length=100)
    smobile = models.CharField(max_length=10)
    saddress= models.CharField(max_length=255)
    Alternate_Contact_NO = models.IntegerField()
    Expriance = models.CharField(max_length=100)
    Privies_salary = models.FloatField()    
    
    
class AddTeacher(models.Model):
    sname = models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric])
    semail = models.EmailField(max_length=100)
    smobile = models.CharField(max_length=10)
    saddress= models.CharField(max_length=255)
    Alternate_Contact_NO = models.IntegerField()
    Expriance = models.CharField(max_length=100)
    Privies_salary = models.FloatField()  
    
    
# class Designation(models.Model):
#     name = models.CharField(max_length=100)
#     Powered = models.ForeignKey(Power,on_delete=models.CASCADE)
    
    
# class Power(models.Model):
#     add_employee = models.CharField(max_length=100)
#     add_designation = models.CharField(max_length=100)
#     edit_employee = models.CharField(max_length=100)
#     view_employee = models.CharField(max_length=100)
#     # upload_data = models.FileField(upload_to ='uploads/')
#     upload_data = models.CharField(max_length=100)
#     assign_data = models.CharField(max_length=100)
#     view_attendance = models.CharField(max_length=100)
#     filter_data = models.CharField(max_length=100)
#     view_deshboard = models.CharField(max_length=100)
#     birthday_wishos = models.CharField(max_length=100)
#     send_post = models.CharField(max_length=100)
#     fatch_data = models.CharField(max_length=100)
#     view_data = models.CharField(max_length=100)
#     edit_data = models.CharField(max_length=100)
#     create_data = models.CharField(max_length=100)
#     send_mamo = models.CharField(max_length=100)
#     create_subject = models.CharField(max_length=100)
#     edit_courses = models.CharField(max_length=100)
#     add_courses = models.CharField(max_length=100)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        