from django.db import models
from student_records.models import Student
from course_info.models import Course

# Create your models here.
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'course']
    
    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"
    