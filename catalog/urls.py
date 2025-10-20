from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductTemplateView, ContactFormView, ProductDetailView, ProductCreateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', ProductListView.as_view(), name='product_list'),
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('', ContactFormView.as_view(), name='answer'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/new/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductDetailView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
