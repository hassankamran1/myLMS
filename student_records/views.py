from django.shortcuts import get_object_or_404, render
from .models import Student

#view for student views

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_records/student_list.html', {'students': students})

def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_records/student_profile.html', {'student': student})