from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'preview', 'publication_sign']
    success_url = reverse_lazy('blog:articles_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'preview', 'publication_sign']
    success_url = reverse_lazy('blog:articles_list')


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles_list')