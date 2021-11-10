from django.urls import path
from .views import search,rest_api_search


urlpatterns = [
    path('',search,name='search'),
    path('api/',rest_api_search,name='search'),
]