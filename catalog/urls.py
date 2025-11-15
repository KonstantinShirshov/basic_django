from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductTemplateView, ContactFormView, ProductDetailView, ProductCreateView, \
    ProductDeleteView, ProductUpdateView, UnpublishProductView, ProductCategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', ProductListView.as_view(), name='product_list'),
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('', ContactFormView.as_view(), name='answer'),
    path('products/<int:pk>/', cache_page(60 * 2)(ProductDetailView.as_view()), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/unpublish/', UnpublishProductView.as_view(), name='product_unpublish'),
    path('products/category/<int:category_id>/', ProductCategoryListView.as_view(), name='product_category_list'),

]
