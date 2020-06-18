from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post

# Create your views here.
class BlogListView(ListView):
  template_name = 'list.html'
  model = Post

class BlogDetailView(DetailView):
  template_name = 'detail.html'
  model = Post

class BlogCreateView(CreateView):
  template_name = 'create.html'
  model = Post
  fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
  template_name = 'update.html'
  model = Post
  fields = ['title', 'body']

class BlogDeleteView(DeleteView):
  template_name = 'delete.html'
  model = Post
  success_url = reverse_lazy('list')
