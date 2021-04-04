from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import( CreateView, UpdateView,\
    DeleteView )
from django.urls import reverse_lazy # new
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



class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'pages/post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'pages/post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('pages:home')