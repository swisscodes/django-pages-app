from django.shortcuts import render
from django.views.generic import DetailView, ListView
from . models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'pages/home.html'
    context_object_name = 'all_post'



class PagesView(DetailView):
    model = Post
    template_name = 'pages/detail.html'
    context_object_name = 'post_detail'