from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from slugify import slugify


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=110)
    content = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='images/blog_photos', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    post_slug = models.SlugField(default='', max_length=100)  # new


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.post_slug})
    
    def save(self, *args, **kwargs):
        if not self.post_slug:
            self.post_slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

        
    



