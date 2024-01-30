from course import views
from django.urls import path
urlpatterns = [
       path('', views.subj),
       path('regfor/',views.regfor,),
       path('save/',views.saver)
]
