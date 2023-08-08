"""
URL configuration for hw4_blog_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import statistics
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import home_view, profile_view, post_view, post_detail, post_update, delete_post
from users.views import loginUser, registerUser, logoutUser


urlpatterns = [
    path('', home_view, name= 'home_view'),
    path('admin/', admin.site.urls),
    path('login/', loginUser, name= 'login' ),
    path('register/', registerUser, name= 'register' ),
    path('logout/', logoutUser, name='logout' ),
    path('profile/', profile_view, name='profile'),
    path('post/', post_view, name='post'),
    path('post_detail/<slug:post_slug>/', post_detail, name='post_detail'),
    path('post_update/<slug:post_slug>', post_update, name='post_update'),
    path('delete_post/<slug:post_slug>', delete_post, name='delete_post')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
