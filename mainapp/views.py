from django.shortcuts import render, get_object_or_404, redirect
from .models import PoetryPost, PhotographyPost

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
from .models import PoetryPost, PhotographyPost


def poetry_list(request):
    posts = PoetryPost.objects.all().order_by('category')
    cat='All'
    num_posts=posts.count()
    return render(request, 'blog/poetry_list.html', {'posts': posts,'category': cat,'lengthOfPosts': num_posts})

def poetry_detail(request, pk):
    post = get_object_or_404(PoetryPost, pk=pk)
    cat=post.category
    return render(request, 'blog/poetry_detail.html', {'post': post,'category': cat})

def photography_list(request):
    posts = PhotographyPost.objects.all()
    cat='Photography'
    num_posts=posts.count()
    return render(request, 'blog/photography_list.html', {'posts': posts,'category':cat})

def photography_detail(request, pk):
    post = get_object_or_404(PhotographyPost, pk=pk)
    cat='Photography'
    return render(request, 'blog/photography_detail.html', {'post': post,'category':cat})

def photography_featured_images(request, pk):
    post = get_object_or_404(PhotographyPost, pk=pk)
    return render(request, 'blog/photography_featured_images.html', {'post': post})

def shortstories_list(request):
    posts = PoetryPost.objects.all().filter(category='Short-Story')
    cat='Short stories'
    num_posts=posts.count()
    return render(request, 'blog/poetry_list.html', {'posts': posts,'category': cat,'lengthOfPosts': num_posts})

def opinions_list(request):
    posts = PoetryPost.objects.all().filter(category='Opinion')
    cat='Opinions'
    num_posts=posts.count()
    return render(request, 'blog/poetry_list.html', {'posts': posts,'category': cat,'lengthOfPosts': num_posts})

def poetry_only(request):
    posts = PoetryPost.objects.all().filter(category='Poetry')
    cat='Poetry'
    num_posts=posts.count()
    return render(request, 'blog/poetry_list.html', {'posts': posts,'category': cat,'lengthOfPosts': num_posts})

class PoetryPostUpdateView(UpdateView):
    model = PoetryPost
    fields = ['title', 'text', 'image']
    template_name_suffix = '_update_form'

class PoetryPostDeleteView(DeleteView):
    model = PoetryPost
    success_url = reverse_lazy('poetry_list')

class PhotographyPostUpdateView(UpdateView):
    model = PhotographyPost
    fields = ['title', 'description', 'main_image', 'featured_images']
    template_name_suffix = '_update_form'

class PhotographyPostDeleteView(DeleteView):
    model = PhotographyPost
    success_url = reverse_lazy('photography_list')
class PoetryPostCreateView(CreateView):
    model = PoetryPost
    fields = ['title', 'content', 'image']
    template_name = 'blog/poetrypost_form.html'
    success_url = reverse_lazy('poetry_list')

class PhotographyPostCreateView(CreateView):
    model = PhotographyPost
    fields = ['title', 'description', 'main_image', 'featured_images']
    template_name = 'blog/photographypost_form.html'
    success_url = reverse_lazy('photography_list')
