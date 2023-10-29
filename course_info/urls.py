from django.urls import path
from . import views

app_name = 'course_info'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
]
