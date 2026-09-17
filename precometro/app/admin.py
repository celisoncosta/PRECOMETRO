
from django.contrib import admin

from .models import Produto, Supermercado, Preco

# Register your models here.
admin.site.register(Produto)
admin.site.register(Supermercado)
admin.site.register(Preco)


