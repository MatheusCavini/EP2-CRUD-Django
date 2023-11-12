from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import CommentForm, PostForm
from django.views import generic
from datetime import datetime




class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.date = datetime.now()
        post_thumb = form.cleaned_data['thumb']
        post_image = form.cleaned_data['img2']
        post_text1 = form.cleaned_data['text1']
        post_text2 = form.cleaned_data['text2']
        post.content = f'<section class="ProjectContent"><p class="ProjectText">{post_text1}</p><img class="ProjectImage" src="{post_thumb}" title="source: imgur.com" /><p class="ProjectText">{post_text2}</p><img  class="ProjectImage" src="{post_image}" title="source: imgur.com" /></section>'
        post.text1 = post_text1
        post.text2 = post_text2
        post.img2 = post_image
        post.save()

        return HttpResponseRedirect(reverse('posts:detail', args=(post.id,)))

class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy("posts:index")

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'
    success_url = reverse_lazy('posts:detail')

    def form_valid(self, form):
        post = form.instance
        post_title = form.cleaned_data['title']
        post_thumb = form.cleaned_data['thumb']
        post_image = form.cleaned_data['img2']
        post_text1 = form.cleaned_data['text1']
        post_text2 = form.cleaned_data['text2']
        post.title = post_title
        post.date = datetime.now()
        post.thumb = post_thumb
        post.content = '<section class="ProjectContent"><p class="ProjectText">' + post_text1 + '</p><img class="ProjectImage" src="'+post_thumb+'" title="source: imgur.com" /><p class="ProjectText">' + post_text2 + '</p><img class="ProjectImage" src="'+post_image+'" title="source: imgur.com" /></section>'
        post.text1 = post_text1
        post.text2 = post_text2
        post.img2 = post_image
        post.save()
        return HttpResponseRedirect(
                reverse('posts:detail', args=(post.id, )))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.object
        return context

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
