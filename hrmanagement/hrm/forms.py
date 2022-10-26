from pyexpat import model
from attr import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User

# class SignUpForm(forms.ModelForm):
#     # password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
#     # email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
#     class Meta:
#         model = User
#         fields = ['name', 'email', 'password']
#         labels = {'email': 'Email', 'name':'Name'}
#         widgets={
#             'name': forms.TextInput(),
#             'email': forms.EmailInput(),
#             'password': forms.PasswordInput(render_value=True),
#         }

