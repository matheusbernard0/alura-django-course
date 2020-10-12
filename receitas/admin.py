from django.contrib import admin
from .models import Receita


class ListaReceitas(admin.ModelAdmin):
    list_display = ('nome_receita', 'categoria', 'tempo_preparo', 'publicada')
    list_display_links = ('nome_receita', 'categoria', 'tempo_preparo')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 1


admin.site.register(Receita, ListaReceitas)
