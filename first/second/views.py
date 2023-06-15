import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def f4(request):
   return render(request,'fa.html',{'d':datetime.datetime.now(),'t':'true'})
   
