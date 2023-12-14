''' blog/views.py'''

# Imports
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    '''
    post_list function

    1. Get a list of all the posts in the database and pass it to the template.
    2. Render the template.
    '''
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    '''
    post_detail function
    
    1. Get a single post from the database using the primary key (pk) passed in the URL.
    2. Render the template.
    '''
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
