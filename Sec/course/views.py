from django.shortcuts import render
from course.forms import RegistrationForm

def subj(request):
    return render(request, 'course/topic.html')

def regfor(request):
    a=RegistrationForm()
    return render(request, 'course/regfor.html',{'form':a})