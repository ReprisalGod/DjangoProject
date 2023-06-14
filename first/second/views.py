from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def f4(request):
   return HttpResponse("Second is running")
   
