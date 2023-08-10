import statistics
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog.views import home_view, post_view, post_detail, post_update, delete_post
from users.views import loginUser, registerUser, logoutUser, profile_view, profile_update


urlpatterns = [
    path('', home_view, name= 'home_view'),
    path('admin/', admin.site.urls),
    path('login/', loginUser, name= 'login' ),
    path('register/', registerUser, name= 'register' ),
    path('logout/', logoutUser, name='logout' ),
    path('post/', post_view, name='post'),
    path('post_detail/<slug:post_slug>/', post_detail, name='post_detail'),
    path('post_update/<slug:post_slug>', post_update, name='post_update'),
    path('delete_post/<slug:post_slug>', delete_post, name='delete_post'),
    path('profile/<slug:profile_slug>/', profile_view, name='profile_view'),
    path('profile_update/<slug:profile_slug>/', profile_update, name='profile_update')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
