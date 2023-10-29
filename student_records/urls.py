from django.urls import path
from . import views

app_name = 'student_records'

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_profile, name='student_profile'),
]
