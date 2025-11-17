from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect

from config.settings import CACHE_ENABLED
from .forms import ContactForm, ProductForm
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, FormView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product
from .services import get_category_products


class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)

        if request.user.has_perm('catalog.can_unpublish_product'):
            product.is_published = not product.is_published
            product.save()
            return redirect('catalog:product_list')
        return HttpResponseForbidden("У вас нет прав для публикации продукта.")


class ProductCategoryListView(ListView):
    model = Product
    template_name = 'catalog\product_category_list.html'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return get_category_products(category_id)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog\home.html'

    def get_queryset(self):
        if not CACHE_ENABLED:
            queryset = Product.objects.filter(is_published=True)
            if self.request.user.has_perm('catalog.can_unpublish_product'):
                queryset = Product.objects.all()
            return queryset
        cache_key = f"product_list_{self.request.user.username}_can_unpublish_{self.request.user.has_perm('catalog.can_unpublish_product')}"
        products = cache.get_or_set(cache_key, lambda: Product.objects.filter(is_published=True), timeout=300)
        return products



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

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != request.user:
            return HttpResponseForbidden("У вас нет прав для редактирования этого продукта.")
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('catalog:product_update', args=[self.kwargs.get('pk')])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)

        if not (request.user.has_perm('catalog.delete_product') or request.user == product.owner):
            return HttpResponseForbidden("У вас нет прав для удаления продукта.")

        # Логика исключения продукта
        product.delete()

        return redirect('catalog:product_list')



class ContactFormView(FormView):
    template_name = 'catalog\contacts.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        # Другие действия с данными формы
        return HttpResponse(f'Спасибо, {name}! Мы с вами свяжемся в ближайшее время.')
