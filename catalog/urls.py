from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductTemplateView, ContactFormView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', ProductListView.as_view(), name='index'),
    path('contacts/', ProductTemplateView.as_view(), name='contacts'),
    path('', ContactFormView.as_view(), name='answer'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail')
]
