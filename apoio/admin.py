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
from .models import EixoPlano, Ano, TipoPrograma, TipoAcao

# Eixos do Plano #
@admin.register(EixoPlano) # chama diretamente
class EixoPlanoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("nome",)

@admin.register(Ano) # chama diretamente
class AnoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("ano_nr",)

@admin.register(TipoPrograma) # chama diretamente
class TipoProgramaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("tipo_programa_nm",)

@admin.register(TipoAcao) # chama diretamente
class TipoAcaoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("tipo_acao_nm",)