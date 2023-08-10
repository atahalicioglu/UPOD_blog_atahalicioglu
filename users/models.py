from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from slugify import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)   # olmasi gereken charfield, 
    surname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/user_photos', null=True)
    profile_slug = models.SlugField(default='', max_length=100)  

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("profile_view", kwargs={"slug": self.profile_slug})
    
    def save(self, *args, **kwargs):
        if not self.profile_slug:
            self.profile_slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)