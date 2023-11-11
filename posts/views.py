from django.shortcuts import render
from .models import Post


def list_posts(request):
    posts_list = Post.objects.all()
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)

def detail_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

# Create your views here.
