from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse


def list_posts(request):
    posts_list = Post.objects.all()
    context = {'posts_list': posts_list}
    return render(request, 'posts/index.html', context)

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'posts/detail.html', context)

def create_post(request):
    if request.method == 'POST':
        post_title = request.POST['name']
        post_date = '2023-11-11'
        post_thumb = request.POST['first_img']
        post_image = request.POST['second_img']
        post_text1 = request.POST['first_text']
        post_text2 = request.POST['second_text']
        post = Post(title=post_title,
                      date=post_date,
                      thumb=post_thumb,
                      content= '<section class="ProjectContent"><p class="ProjectText">' + post_text1 + '</p><img class="ProjectImage" src="'+post_thumb+'" title="source: imgur.com" /><p class="ProjectText">' + post_text2+'</p><img  class="ProjectImage" src="'+post_image+'" title="source: imgur.com" /></section>'
                      )
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        return render(request, 'posts/create.html', {})


# Create your views here.
