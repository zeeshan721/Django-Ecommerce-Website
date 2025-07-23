from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from ecommerceapp.models import Contact,Product
import re
from django.shortcuts import render,redirect

# Create your views here.


def index(request):
    products = Product.objects.all()  # fetch all products
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        if not name or any(char.isdigit() for char in name):
            messages.error(request,'Invalid name : Name should not contain numbers')
            
        elif not re.match(r"^\S+@\S+\.\S+$", email):
            messages.error(request,'Invalid email address')
        elif not re.match(r"^\d{11}$", phone):
            messages.error(request, 'Phone number must be 11 digit')  

        else:
            contact = Contact(name=name,email=email,phone=phone,desc=desc, date = datetime.today())
            contact.save()
            messages.success(request, 'Your form has been submited succesfuly!!')
            
    return render(request, 'contact.html')