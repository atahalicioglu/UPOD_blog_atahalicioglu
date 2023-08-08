from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import BlogPost
from django.contrib import messages
from slugify import slugify


# Create your views here.

def home_view(request):

    blog_posts = {'blog_posts': [post for post in BlogPost.objects.all() if not post.is_deleted]}

    return render(request, 'blog/home_page.html', blog_posts)

@login_required(login_url='/login/')
def profile_view(request):
    context = {}
    return render(request, 'blog/profile.html',context)



@login_required(login_url='/login/')
def post_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        photo = request.FILES['photo']

        # Validate the form data (you can add more validation if needed)
        if not title or not content:
            messages.error(request, 'Please fill in all the required fields.')
            return redirect('post_view')

        # Create the blog post object and save it to the database
        blog_post = BlogPost.objects.create(user=request.user, title=title, image=photo, content=content)

        # Optionally, you can display a success message to the user
        messages.success(request, 'Blog post created successfully.')

        # Redirect the user to a different page after the form submission (if needed)
        return redirect('/')

    context = {}
    return render(request, 'blog/post.html', context)

@login_required(login_url='/login/')
def post_detail(request, post_slug):
    post = get_object_or_404(BlogPost, post_slug= post_slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context )

@login_required(login_url='/login/')
def post_update(request, post_slug):

    post = get_object_or_404(BlogPost, post_slug= post_slug)

    
    title = request.POST['title']
    content = request.POST['content']

    if not title or not content:
        messages.error(request, 'Please fill in all the required fields.')
        return redirect('post_view')
        
    new_slug = slugify(title)

    post.title = title
    post.content = content
    post.post_slug = new_slug

    post.save()


    messages.success(request, 'Blog post updated successfully.')


    return redirect('/')



@login_required(login_url='/login/')
def delete_post(request, post_slug):
    post = get_object_or_404(BlogPost, post_slug= post_slug)
    post.is_deleted = True
    post.save()
    context = {}
    return redirect('/' )




