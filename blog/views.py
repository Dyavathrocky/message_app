from django.shortcuts import render

from django.views.generic import ListView

from .models import Post1

# Create your views here.

class BlogListView(ListView):
    model = Post1
    template_name = 'blog_home.html'