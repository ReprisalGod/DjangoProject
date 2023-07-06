from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Student
from .forms import StudentRegistration


# Create your views here.
def f1(request):
    return HttpResponse("<a href=http://127.0.0.1:8000/admin/>Admin</a>")
def f2(request):
    return render(request,'medicare-plus/index.html')

def f3(request):
    st=Student.objects.all()
    return render(request,'ip.html',{'st':st})
def f4(request):
    s=StudentRegistration()
    return render(request,'enrollform.html',{'si':s})
