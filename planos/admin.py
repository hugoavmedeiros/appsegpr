# django #
from django.contrib import admin

# libs #
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import inlineformset_factory
from django.http import HttpResponse
from import_export.admin import ImportExportActionModelAdmin, ImportExportModelAdmin

# models #
from .models import Plano, AcaoPlano

# Eixos do Plano #
@admin.register(Plano) # chama diretamente
class PlanoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("nome",)

@admin.register(AcaoPlano) # chama diretamente
class AcaoPlanoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("eixo", "plano", "nome", "policiais", "diarias", "pjes")