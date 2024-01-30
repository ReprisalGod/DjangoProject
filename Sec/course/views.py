from django.shortcuts import render
from course.forms import RegistrationForm
from .models import Student

def subj(request):
    return render(request, 'course/topic.html')

def regfor(request):
    a=RegistrationForm()
    return render(request, 'course/regfor.html',{'form':a})

def saver(request):
    fm=RegistrationForm(request.POST)
    r=fm.roll
    nm=fm.name
    
    reg=Student(name=nm,roll=r)
    reg.save