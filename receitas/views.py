from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    dados = {
        'nome_das_receitas': {
            1: 'Sorvete',
            2: 'Torta de Limão',
            3: 'Suco de Goiaba',
        }
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')