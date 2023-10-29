from django.shortcuts import render
from .models import Course

#below are views for course_info

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_info/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'course_info/course_detail.html', {'course': course})
