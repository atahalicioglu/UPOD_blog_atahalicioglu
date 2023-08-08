from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.

def loginUser(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
            if user is not None:
                login(request, user)
                messages.success(request, "Logged In Successfully")
                if request.POST.get('next'):
                    return redirect(request.POST.get('next'))
                return redirect('home_view')
            else:
                messages.error(request, "Invalid credentials")
        return render(request, "blog/login.html")
    return redirect("home_view")


def registerUser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_c = request.POST.get("password-c")
        if (password == password_c):
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                messages.success(request, "Logged In Successfully")
                return redirect("home_view")
            except IntegrityError:
                messages.info(request, "Try different Username")
                return render(request, "blog/register.html")
        messages.error(request, "Password doesn't match Confirm Password")
    if request.user.is_authenticated:
        return redirect('home_view')
    return render(request, "blog/register.html")

def logoutUser(request):
    logout(request)
    return redirect('home_view')