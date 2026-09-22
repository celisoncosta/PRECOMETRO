from django.shortcuts import render, redirect
from .models import Supermercado, Produto, Preco


# --- HOME / LISTAGEM COM FILTRO DINÂMICO ---
def home(request):
    # 1. Obtém os parâmetros digitados/selecionados no filtro GET
    filtro_produto = request.GET.get('produto', '')
    filtro_categoria = request.GET.get('categoria', '')

    # 2. Busca inicial de todos os preços
    precos = Preco.objects.all()

    # 3. Aplica os filtros se foram preenchidos na busca
    if filtro_produto:
        precos = precos.filter(produto__nome__icontains=filtro_produto)

    if filtro_categoria:
        precos = precos.filter(produto__categoria__iexact=filtro_categoria)

    # Ordena pelo menor preço
    precos = precos.order_by('valor')

    # 4. Busca no banco as categorias reais e únicas dos produtos cadastrados
    categorias = (
        Produto.objects.exclude(categoria__isnull=True)
        .exclude(categoria__exact='')
        .values_list('categoria', flat=True)
        .distinct()
        .order_by('categoria')
    )

    return render(request, 'home.html', {
        'precos': precos,
        'categorias': categorias,
        'filtro_produto': filtro_produto,
        'filtro_categoria': filtro_categoria,
    })


# --- SUPERMERCADO ---
def supermercado_form(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        s = Supermercado.objects.create(nome=nome)
        print(s.id)
        return redirect('app:home')

    return render(request, 'supermercado_form.html')


def supermercado_edit(request, pk):
    if pk:
        supermercado = Supermercado.objects.get(pk=pk)
    else:
        supermercado = None

    if request.method == 'POST':
        supermercado.nome = request.POST['nome']
        supermercado.save()
        print(supermercado.id)
        return redirect('app:home')

    return render(request, 'supermercado_form.html', {'supermercado': supermercado})


def supermercado_delete(request, pk):
    if pk:
        supermercado = Supermercado.objects.get(pk=pk)
        supermercado.delete()
        return redirect('app:home')


# --- PRODUTO ---
def produto_form(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        marca = request.POST['marca']
        categoria = request.POST['categoria']

        p = Produto.objects.create(nome=nome, marca=marca, categoria=categoria)
        print(p.id)
        return redirect('app:home')

    return render(request, 'produto_form.html')


def produto_edit(request, pk):
    if pk:
        produto = Produto.objects.get(pk=pk)
    else:
        produto = None

    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.marca = request.POST['marca']
        produto.categoria = request.POST['categoria']
        produto.save()
        print(produto.id)
        return redirect('app:home')

    return render(request, 'produto_form.html', {'produto': produto})


def produto_delete(request, pk):
    if pk:
        produto = Produto.objects.get(pk=pk)
        produto.delete()
        return redirect('app:home')


# --- PREÇO: CADASTRO COM DATALIST / AUTOCOMPLETE ---
def preco_form(request):
    if request.method == 'POST':
        supermercado_nome = request.POST.get('supermercado_nome', '').strip()
        produto_str = request.POST.get('produto_nome', '').strip()
        valor = request.POST['valor']

        # Extrai o nome do produto caso venha no formato "Nome (Marca)"
        produto_nome = produto_str.split(' (')[0]

        # Busca os objetos no banco pelo nome digitado/selecionado
        supermercado_obj = Supermercado.objects.filter(nome__iexact=supermercado_nome).first()
        produto_obj = Produto.objects.filter(nome__iexact=produto_nome).first()

        if supermercado_obj and produto_obj:
            pr = Preco.objects.create(
                supermercado=supermercado_obj,
                produto=produto_obj,
                valor=valor
            )
            print(pr.id)

        return redirect('app:home')

    supermercados = Supermercado.objects.all()
    produtos = Produto.objects.all()

    return render(request, 'preco_form.html', {
        'supermercados': supermercados,
        'produtos': produtos
    })


# --- PREÇO: EDIÇÃO COM DATALIST / AUTOCOMPLETE ---
def preco_edit(request, pk):
    if pk:
        preco = Preco.objects.get(pk=pk)
    else:
        preco = None

    if request.method == 'POST' and preco:
        supermercado_nome = request.POST.get('supermercado_nome', '').strip()
        produto_str = request.POST.get('produto_nome', '').strip()

        produto_nome = produto_str.split(' (')[0]

        supermercado_obj = Supermercado.objects.filter(nome__iexact=supermercado_nome).first()
        produto_obj = Produto.objects.filter(nome__iexact=produto_nome).first()

        if supermercado_obj and produto_obj:
            preco.supermercado = supermercado_obj
            preco.produto = produto_obj
            preco.valor = request.POST['valor']
            preco.save()
            print(preco.id)

        return redirect('app:home')

    supermercados = Supermercado.objects.all()
    produtos = Produto.objects.all()

    return render(request, 'preco_form.html', {
        'preco': preco,
        'supermercados': supermercados,
        'produtos': produtos
    })


# --- PREÇO: DELETAR ---
def preco_delete(request, pk):
    if pk:
        preco = Preco.objects.get(pk=pk)
        preco.delete()
        return redirect('app:home')