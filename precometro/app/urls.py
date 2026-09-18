from django import urls
from django.urls import path
from .views import home, preco_form, produto_form, supermercado_form

app_name = "app"
urlpatterns = [
    path('', home, name='home'),
    path('preco/', preco_form, name='preco'),
    path('produto/', produto_form, name='produto'),
    path('supermercado/', supermercado_form, name='supermercado'),
]