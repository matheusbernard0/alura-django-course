from django.shortcuts import render, get_object_or_404

from receitas.models import Receita


def index(request):

    dados = {
        'receitas': Receita.objects.order_by('-date_receita').filter(publicada=True)
    }

    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    dados = {
        'receita': receita
    }

    return render(request, 'receita.html', dados)