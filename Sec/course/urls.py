from course import views
from django.urls import path
urlpatterns = [
       path('', views.subj,{'t':'true','n':'Nikhil'}),
]
