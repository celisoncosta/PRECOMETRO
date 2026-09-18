from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def preco_form(request):
    return render(request, 'preco_form.html')

def produto_form(request):
    return render(request, 'produto_form.html')

def supermercado_form(request):
    return render(request, 'supermercado_form.html')
