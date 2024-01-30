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
from .models import Secretaria, Orgao, AIS, Unidade, Responsavel

# Eixos do Plano #
@admin.register(Secretaria) # chama diretamente
class SecretariaAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("nome",)

@admin.register(Orgao) # chama diretamente
class OrgaoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("nome",)

@admin.register(AIS) # chama diretamente
class AISAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("sigla",)

@admin.register(Unidade) # chama diretamente
class UnidadeAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("sigla",)

@admin.register(Responsavel) # chama diretamente
class ResponsavelAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = ("nome",)