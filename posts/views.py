from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CommentForm, PostForm

from datetime import datetime


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
        form = PostForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            post_date = datetime.now()
            post_thumb = form.cleaned_data['thumb']
            post_image = form.cleaned_data['img2']
            post_text1 = form.cleaned_data['text1']
            post_text2 = form.cleaned_data['text2']
            post = Post(title=post_title,
                        date=post_date,
                        thumb=post_thumb,
                        content= '<section class="ProjectContent"><p class="ProjectText">' + post_text1 + '</p><img class="ProjectImage" src="'+post_thumb+'" title="source: imgur.com" /><p class="ProjectText">' + post_text2+'</p><img  class="ProjectImage" src="'+post_image+'" title="source: imgur.com" /></section>',
                        text1 = post_text1,
                        text2 = post_text2,
                        img2 = post_image)
            post.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/create.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))

    context = {'post': post}
    return render(request, 'posts/delete.html', context)

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post_title = form.cleaned_data['title']
            post_date = datetime.now()
            post_thumb = form.cleaned_data['thumb']
            post_image = form.cleaned_data['img2']
            post_text1 = form.cleaned_data['text1']
            post_text2 = form.cleaned_data['text2']
            post.title =post_title
            post.date =post_date
            post.thumb =post_thumb
            post.content = '<section class="ProjectContent"><p class="ProjectText">' + post_text1 + '</p><img class="ProjectImage" src="'+post_thumb+'" title="source: imgur.com" /><p class="ProjectText">' + post_text2+'</p><img  class="ProjectImage" src="'+post_image+'" title="source: imgur.com" /></section>'
            post.text1 = post_text1
            post.text2 = post_text2
            post.img2 = post_image            
            post.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={
                'title': post.title,
                'text1': post.text1,
                'text2': post.text2,
                'thumb': post.thumb,
                'img2': post.img2
            })
        context = {'post': post, 'form': form}
        return render(request, 'posts/update.html', context)

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            project=post, 
                            date = datetime.now())
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post':post}
    return render(request, 'posts/comment.html', context)
