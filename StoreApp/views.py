from django.shortcuts import render
from StoreApp.models import Departamento, Produto

# Create your views here.
def index(request):
    # orm busca os departamentos e produto no banco de dados
    departamentos = Departamento.objects.all()
    produtos = Produto.objects.all()
    
    context = {
        'departamentos': departamentos,
        'produtos': produtos
    }

    return render(request, 'index.html', context)


def produtos(request):
    context = {}

    return render(request, 'produtos.html', context)