from .forms import ContactForm, ProductForm
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog\home.html'


class ProductTemplateView(TemplateView):
    model = Product
    template_name = 'catalog\contacts.html'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog\product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_update', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactFormView(FormView):
    template_name = 'catalog\contacts.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        # Другие действия с данными формы
        return HttpResponse(f'Спасибо, {name}! Мы с вами свяжемся в ближайшее время.')
