from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

from vendor.models import Contact
from django.views.decorators.csrf import csrf_exempt
from .forms import contactform

from django.views.generic import view 

# Create your views here.
#create
@csrf_exempt
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        addr=request.POST.get('addr')
        contact=Contact(name=name, email=email, phone=phone, addr=addr)
        contact.save()
        print("Data save in database successfully")
    return render(request, 'contacts.html')
