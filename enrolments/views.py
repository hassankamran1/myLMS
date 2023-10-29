from django.shortcuts import render, redirect
from .models import Enrollment
from course_info.models import Course
from student_records.models import Student

#views for enrolment apps
def enrolled_students(request, course_id):
    enrollments = Enrollment.objects.filter(course_id=course_id)
    return render(request, 'enrolments/enrolled_students.html', {'enrollments': enrollments})

def manage_enrolments(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')
        student = Student.objects.get(pk=student_id)
        course = Course.objects.get(pk=course_id)
        Enrollment.objects.create(student=student, course=course)
        return redirect('enrolments:enrolled_students', course_id=course_id)
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'enrolments/manage_enrolments.html', {'students': students, 'courses': courses})
