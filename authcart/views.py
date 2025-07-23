from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login




def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')

        if password != confirm_password:
            messages.error(request, "Your password does not match")
            return render(request, 'authentication/signup.html')

        if User.objects.filter(username=email).exists():
            messages.warning(request, "The username/email is already taken ")
            return render(request, 'authentication/signup.html')

        User.objects.create_user(username=email,email=email,password=password)
        messages.success(request, "This user has been created successfully")
        return redirect('signup')  # Use the name you gave this route in urls.py

    return render(request, 'authentication/signup.html')


def handlelogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass1')

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('/')  # Redirect to homepage or dashboard
        else:
            messages.error(request, 'Invalid email or password')
            return render(request, 'authentication/login.html')

    return render(request, 'authentication/login.html')

def handlelogout(request):
        logout(request)
        messages.info(request,'You Succesfuly Logout!!')
        return redirect('/auth/login')  # Use URL name from urls.py
