from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

from django.shortcuts import render
from django.utils import timezone
from .models import Post
def post_list(request):
    posts = Post.objects.filter(published_dated__lte=timezone.now()).order_by('published_dated')
    return render(request, 'blog/post_list.html', {'posts': posts})
