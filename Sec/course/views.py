from django.shortcuts import render

def subj(request):
    return render(request, 'course/topic.html')

