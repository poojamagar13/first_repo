from django.contrib import admin
from django.urls import path
from employee_info import views



urlpatterns = [
    path('first/',views.first_fun),
]
