from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    return HttpResponse("<a href=http://127.0.0.1:8000/admin/>Admin</a>")
def f2(request):
    return HttpResponse("<h1>Click above link to go to admin page</h1>")
