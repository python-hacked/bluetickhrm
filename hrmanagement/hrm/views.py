from django.shortcuts import render, redirect, HttpResponseRedirect
from hrm.models import AddCourses, AddStudents, User,AddTeacher,AddHr
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
from django.contrib.auth import logout
from django.http import HttpResponse,JsonResponse
import json


# Create your views here.

def index(request):
    return render(request, 'hrm/index.html')

def signup(request):
    return render(request, 'hrm/sign-up.html')

def dashboard(request):
    addcourses= AddCourses.objects.all()
    totalcourse=AddCourses.objects.all().count()
    totalstudent=AddStudents.objects.all().count()
    return render(request, 'hrm/dashboard.html',{'addcourses':addcourses, 'totalcourse':totalcourse, 'totalstudent':totalstudent})

def courses(request):
    stu = AddCourses.objects.filter(is_active=True).order_by('id')
    return render(request, 'hrm/courses.html', 
                  { 'request':request,
                      'stu':stu,
                   
                    #   'stu':AddCourses.objects.all()
                   }
                  )

def viewstudents(request):
    stu=AddStudents.objects.all()
    addcourses= AddCourses.objects.all()
    redirect("viewstudents")
    return render(request, 'hrm/viewstudents.html', {'stu':stu, 'addcourses':addcourses})

def viewteacher(request):
    stu=AddTeacher.objects.all()
    redirect("viewteacher")
    return render(request, 'hrm/teacher.html', {'stu':stu})

def viewhr(request):
    stu=AddHr.objects.all()
    redirect("viewhr")
    return render(request, 'hrm/hr.html', {'stu':stu})

def notifications(request):
    return render(request, 'hrm/notifications.html')

def profile(request):
    return render(request, 'hrm/profile.html')

def tables(request):
    return render(request, 'hrm/tables.html')

def tenants(request):
    return render(request, 'hrm/tenants.html')

#Signup Form Function
def formdata(request):
    if request.method == 'POST':
        name = request.POST['Name']
        e_mail = request.POST['Email']
        password = make_password(request.POST['Password'])
        if User.objects.filter(email=e_mail).exists():
            messages.error(request, "Email id already exists")
            return redirect('signup')
        else:
            User.objects.create(name=name, email=e_mail, password=password)
            messages.success(request, "Registered Successfully!!")
            return redirect('signup')
                
#Login View Functions
def loginform(request):
    if request.method == "POST":
        email = request.POST['Email']
        User_password = request.POST['Password']
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password
            if check_password(User_password, password):
                return redirect('/dashboard/')
            else:
                messages.error(request, 'Password incorrect')
                return redirect('login')
        else:
            messages.error(request, 'Email is not registered')
            return redirect('login')

def addcourses(request):
    if request.method == "POST":
        c_name= request.POST['CourseName']
        c_fees= request.POST['CourseFees']
        c_duration= request.POST['Duration']
        c_desc= request.POST['CourseDesc']
        messages.success(request, "Course Added Successfully!!")
        AddCourses.objects.create(course=c_name, fees=c_fees, duration= c_duration, desc=c_desc)
        return redirect('courses'
                      )


def addstudent(request):
        if request.method == "POST":
            stu_name= request.POST.get("Name")
            stu_email= request.POST.get("Email")
            stu_mobile= request.POST.get("Mobile")
            stu_college= request.POST.get("College")
            stu_degree= request.POST.get("Degree")
            stu_address= request.POST.get("Address")
            stu_addcourse_id = request.POST.get("course")
            total_amount= request.POST.get("qty")
            paid_amount= request.POST.get("cost")
            due_amount= request.POST.get("DueAmount")
            stu_c9ourse= AddCourses.objects.get(id=stu_addcourse_id)
            if AddStudents.objects.filter(semail=stu_email).exists():
                messages.error(request, "Email id already exists")
                return redirect('addstudent')
        
            elif AddStudents.objects.filter(smobile=stu_mobile).exists():
                messages.error(request, "Mobile Number already exists")
                return redirect('addstudent')
            else:
                AddStudents.objects.create( sname=stu_name, 
                                            semail=stu_email, 
                                            smobile=stu_mobile,
                                            scollege=stu_college,
                                            sdegree=stu_degree,
                                            saddress=stu_address,
                                            scourse=stu_course,
                                            total_amount=total_amount,
                                            paid_amount=paid_amount,
                                            due_amount=due_amount,
                                            )
                messages.success(request, "Student Added Successfully!!")
                stu=AddStudents.objects.all()
                addcourses= AddCourses.objects.all()
                return render(request, 'hrm/viewstudents.html', {'stu':stu, 'addcourses':addcourses,
                                                                 })
        else:
            stu=AddStudents.objects.all()
            addcourses= AddCourses.objects.all()
            return render(request, 'hrm/viewstudents.html', {'stu':stu, 'addcourses':addcourses})
        
          
# Students Search Funcation       
def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(sname__icontains=q) | Q(semail__icontains=q))|Q(smobile__icontains=q)
        stu = AddStudents.objects.filter(multiple_q)
    else:
        stu = AddStudents.objects.all()
    context = {
        'stu': stu
    }
    return render(request, 'hrm/viewstudents.html', context)

# Add Teachers 
def addteacher(request):
        if request.method == "POST":
            stu_name= request.POST.get("Name")
            stu_email= request.POST.get("Email")
            stu_mobile= request.POST.get("Mobile")
            stu_address= request.POST.get("Address")
            Alternate_Contact_NO= request.POST.get("qty")
            Expriance= request.POST.get("cost")
            Privies_salary= request.POST.get("DueAmount")
            if AddTeacher.objects.filter(semail=stu_email).exists():
                messages.error(request, "Email id already exists")
                return redirect('addteacher')
        
            elif AddTeacher.objects.filter(smobile=stu_mobile).exists():
                messages.error(request, "Mobile Number already exists")
                return redirect('addteacher')
            else:
                AddTeacher.objects.create( sname=stu_name, 
                                            semail=stu_email, 
                                            smobile=stu_mobile,
                                            saddress=stu_address,
                                            Alternate_Contact_NO=Alternate_Contact_NO,
                                            Expriance=Expriance,
                                            Privies_salary=Privies_salary,
                                            )
                messages.success(request, "HR Added Successfully!!")
                stu=AddTeacher.objects.all()
                return render(request, 'hrm/teacher.html', {'stu':stu,
                                                                 })
        else:
            stu=AddTeacher.objects.all()
            return render(request, 'hrm/teacher.html', {'stu':stu})

def addhr(request):
        if request.method == "POST":
            stu_name= request.POST.get("Name")
            stu_email= request.POST.get("Email")
            stu_mobile= request.POST.get("Mobile")
            stu_address= request.POST.get("Address")
            Alternate_Contact_NO= request.POST.get("qty")
            Expriance= request.POST.get("cost")
            Privies_salary= request.POST.get("DueAmount")
            if AddHr.objects.filter(semail=stu_email).exists():
                messages.error(request, "Email id already exists")
                return redirect('addhr')
        
            elif AddHr.objects.filter(smobile=stu_mobile).exists():
                messages.error(request, "Mobile Number already exists")
                return redirect('addhr')
            else:
                AddHr.objects.create( sname=stu_name, 
                                            semail=stu_email, 
                                            smobile=stu_mobile,
                                            saddress=stu_address,
                                            Alternate_Contact_NO=Alternate_Contact_NO,
                                            Expriance=Expriance,
                                            Privies_salary=Privies_salary,
                                            )
                messages.success(request, "HR Added Successfully!!")
                stu=AddHr.objects.all()
                return render(request, 'hrm/hr.html', {'stu':stu,
                                                                 })
        else:
            stu=AddHr.objects.all()
            return render(request, 'hrm/hr.html', {'stu':stu})
               

def update_view(request, uid):
    res = AddCourses.objects.get(id=uid)
    return render(request, 'hrm/updatecourse.html', context={
        'stu': res,
    })


def update_course(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        c_name= request.POST['CourseName']
        c_fees= request.POST['CourseFees']
        c_duration= request.POST['Duration']
        c_desc= request.POST['CourseDesc']
        AddCourses.objects.filter(id=uid).update(course=c_name, fees=c_fees, 
                                                duration= c_duration,
                                                desc=c_desc)
        return redirect('/courses/')                
    

def delete(request,pk):   
        AddCourses.objects.filter(id=pk).delete()
        return redirect('courses')    
    