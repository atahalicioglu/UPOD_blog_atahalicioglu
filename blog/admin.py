from django.contrib import admin
from .models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'created_at', 'updated_at', 'is_deleted' )


admin.site.register(BlogPost, BlogPostAdmin)
