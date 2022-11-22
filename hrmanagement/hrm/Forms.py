from django import forms
from .models import AddCourses

class addcoursesforms(forms.ModelForm):
    class Meta:
        model=AddCourses
        fields="__all__"
