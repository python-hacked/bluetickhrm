from django.contrib import admin
from django.urls import path
from hrm import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='login'),
    path('signup/', views.signup, name='signup'),
    path('formdata/', views.formdata, name='form'),
    path('loginform/', views.loginform, name='form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.courses, name='courses'),
    path('addcourses/', views.addcourses, name='addcourses'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('notifications/', views.notifications, name='notifications'),
    path('profile/', views.profile, name='profile'),
    path('tables/', views.tables, name='tables'),
    path('tenants/', views.tenants, name='tenants'),
    path('viewstudents/', views.viewstudents, name='viewstudents'),
    path('search/', views.search, name='search'),
    
    # path('employee/', views.employee, name='employee'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)