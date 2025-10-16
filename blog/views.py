from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from blog.models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_object(self, queryset=None):
        self.article=super().get_object(queryset)
        self.article.views_counter += 1
        self.article.save()
        return self.article


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:articles_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse('blog:article_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles_list')