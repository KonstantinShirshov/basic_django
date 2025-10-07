from itertools import product

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, answer, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('', answer, name='answer'),
    path('products/<int:pk>/', product_detail, name='product_detail')
]
