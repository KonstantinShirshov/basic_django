from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, answer

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('', answer, name='answer')
]
