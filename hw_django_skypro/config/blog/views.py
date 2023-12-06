from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
import uuid


def blog_post_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})


def blog_post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)

    post.views_count += 1
    post.save()

    return render(request, 'blog/post_detail.html', {'post': post})


def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = str(uuid.uuid4())[:8]
            post = form.save()
            return redirect('blog:blog_post_detail', slug=post.slug)
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def blog_post_edit(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:blog_post_detail', slug=post.slug)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


def blog_post_delete(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.delete()
    return redirect('blog_post_list')
