from django.shortcuts import render, get_object_or_404

from receitas.models import Receita


def index(request):

    dados = {
        'receitas': Receita.objects.order_by('-data_receita').filter(publicada=True)
    }

    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    dados = {
        'receita': receita
    }

    return render(request, 'receita.html', dados)


def buscar(request):
    lista_receitas = Receita.objects.filter(nome_receita__icontains=request.GET['buscar'])

    if 'buscar' in request.GET:
        lista_receitas = lista_receitas.order_by('-data_receita')

    return render(request, 'busca.html', {'receitas': lista_receitas})
