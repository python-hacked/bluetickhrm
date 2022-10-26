from django.contrib import admin
from .models import (
    User,AddCourses,AddStudents
)
# Register your models here.
@admin.register((User))
class UserModelAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'password',]

@admin.register((AddCourses))
class AddCoursesModelAdmin(admin.ModelAdmin):
    list_display=['course', 'fees', 'duration','desc']

@admin.register((AddStudents))
class AddStudentsModelAdmin(admin.ModelAdmin):
    list_display=['sname', 'semail', 'smobile','saddress', 'scollege', 'sdegree','scourse','total_amount','paid_amount','due_amount']