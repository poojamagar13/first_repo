from django.shortcuts import render
from django.http import HttpResponse
#function based view
def student_fun(request):
    return HttpResponse('Hello brainworks')

# Create your views here.
