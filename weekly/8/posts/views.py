from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'all_posts': posts
    }
    return render(request, 'posts/index.html', context) 

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'posts/create.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentForm() 
    context = {
        'post': post,
        'comment_form': comment_form 
    }
    return render(request, 'posts/detail.html', context)

def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post) 
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', pk=pk)
    else:
        form = PostForm(instance = post)
    context = {
        'form':form, 
        'post':post
    }
    return render(request, 'posts/update.html', context)
        
def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:index')

def comment_create(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:detail', pk=pk)
    else:
        form = CommentForm()
    context = {
        'comment_form': form,
        'post': post
    }
    return render(request, 'posts/detail.html', context)


@require_POST 
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('posts:detail', pk=pk)  