from django.urls import path
from . import views

app_name = 'enrolments'

urlpatterns = [
    path('enroll/', views.manage_enrolments, name='manage_enrolments'),
    path('enrolled/<int:course_id>/', views.enrolled_students, name='enrolled_students'),
]
