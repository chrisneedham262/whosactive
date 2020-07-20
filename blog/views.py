from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm

#def blogHome(request):
    #return render(request, 'blog/home.html', {})

class BlogHomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

class ArticleHomeView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    #fields = '__all__'

class UpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'
    #fields = ['title', 'body']