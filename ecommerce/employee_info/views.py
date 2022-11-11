from django.shortcuts import render
from django.http import HttpResponse
#function based view
def first_fun(request):
    return HttpResponse('Hello team')

def home_fun(request):
    return HttpResponse('<h1>my home page</h1>')

# Create your views here.
