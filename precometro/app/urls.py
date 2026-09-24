from django.urls import path
from .views import (
    home,

    # Supermercado
    supermercado_list,
    supermercado_form,
    supermercado_edit,
    supermercado_delete,

    # Produto
    produto_list,
    produto_form,
    produto_edit,
    produto_delete,

    # Preço
    preco_form,
    preco_edit,
    preco_delete,
)

app_name = "app"

urlpatterns = [
    path('', home, name='home'),

    # Supermercado
    path('supermercado/', supermercado_list, name='supermercado_list'),
    path('supermercado/cadastrar/', supermercado_form, name='supermercado'),
    path('supermercado/editar/<int:pk>/', supermercado_edit, name='supermercado_edit'),
    path('supermercado/deletar/<int:pk>/', supermercado_delete, name='supermercado_delete'),

    # Produto
    path('produto/', produto_list, name='produto_list'),
    path('produto/cadastrar/', produto_form, name='produto'),
    path('produto/editar/<int:pk>/', produto_edit, name='produto_edit'),
    path('produto/deletar/<int:pk>/', produto_delete, name='produto_delete'),

    # Preço
    path('preco/cadastrar/', preco_form, name='preco'),
    path('preco/editar/<int:pk>/', preco_edit, name='preco_edit'),
    path('preco/deletar/<int:pk>/', preco_delete, name='preco_delete'),
]