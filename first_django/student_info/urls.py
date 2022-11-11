from django.urls import path
from student_info import views



urlpatterns = [
    path('student1/',views.student_fun),
]