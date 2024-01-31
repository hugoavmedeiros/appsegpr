# django #
from django.contrib import admin
from django.utils import timezone

# libs #
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import inlineformset_factory
from django.http import HttpResponse
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

# models #
from .models import Plano, AcaoPlano

#### utils ####

# Eixos do Plano #
@admin.register(Plano) # chama diretamente
class PlanoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = (
        "nome",
        "operativa",
        "ais",
        "unidade",
        "responsavel",
        )

@admin.register(AcaoPlano) # chama diretamente
class AcaoPlanoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("nome", "policiais", "diarias", "pjes")

    list_filter = (
        "data_termino",
        "eixo__nome",
        "plano__nome",
        ) # cria filtros
    
    def get_data(self, obj):
        return obj.data_termino

    get_data.short_description = 'Data'