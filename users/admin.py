from django.contrib import admin

from users.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'image' )


admin.site.register(Profile, ProfileAdmin)