from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError

from users.models import Profile

from blog.models import BlogPost

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
    if request.user.is_authenticated:
        return redirect('home_view')
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_c = request.POST.get("password-c")
        if (password == password_c):
            try:
                user = User.objects.create_user(username, email, password)
                profile = Profile.objects.create(user=user)
                profile.save()
                user.save()
                login(request, user)
                messages.success(request, "Logged In Successfully")
                return redirect("home_view")
            except IntegrityError:
                messages.info(request, "Try different Username")
                return render(request, "blog/register.html")
        messages.error(request, "Password doesn't match Confirm Password")
    return render(request, "blog/register.html")

def logoutUser(request):
    logout(request)
    return redirect('home_view')

@login_required(login_url='/login/')
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, profile_slug = profile_slug)
    blog_posts = BlogPost.objects.filter(user=profile.user)
    context = {'profile' : profile, 'blog_posts' : blog_posts}
    return render(request, 'blog/profile.html', context)

@login_required(login_url='/login/')
def profile_update(request, profile_slug):
    if request.method == 'POST':
        name = request.POST.get("name")
        surname = request.POST.get("surname")

        profile = get_object_or_404(Profile, profile_slug=profile_slug)

        profile.name = name
        profile.surname = surname

        profile.save()        
    
        messages.success(request, 'Profile updated successfully.')
        return redirect('/')

    context = {}
    return render(request, 'blog/profile.html', context)