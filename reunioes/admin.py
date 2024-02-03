#### BASE ####
from django.contrib import admin
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

#### LIBS ####
from import_export.admin import ImportExportModelAdmin

#### MODELOS ####
# Modelosl
from .models import Reuniao, Encaminhamento

#### Funções ####
class VencimentoProximoFilter(admin.SimpleListFilter):
    title = 'Vencimento Próximo'
    parameter_name = 'vencimento_proximo'

    def lookups(self, request, model_admin):
        return (
            ('7', 'Nos Próximos 7 Dias'),
            ('today', 'Hoje'),
        )

    def queryset(self, request, queryset):
        if self.value() == '7':
            return queryset.filter(prazo__gte=timezone.now(), prazo__lte=timezone.now() + timezone.timedelta(days=7))
        elif self.value() == 'today':
            return queryset.filter(prazo=timezone.now().date())

#### Reunião ####
@admin.register(Reuniao) # chama diretamente
class ReuniaoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = (
        "politica",
        "data",
        "numero",
        "assunto",
        'link_para_encaminhamentos',
        )
    
    def link_para_encaminhamentos(self, obj):
        url = reverse('admin:reunioes_encaminhamento_changelist')  
        url += f'?reuniao_id={obj.id}'  
        return format_html('<a class="button" href="{}">Consultar Encaminhamentos</a>', url)
    link_para_encaminhamentos.short_description = 'Encaminhamentos'

#### Encaminhamentos ####
@admin.register(Encaminhamento) # chama diretamente
class EncaminhamentoAdmin(ImportExportModelAdmin): # lista_display permite mostrar campos customizados
    list_display = (
        "encaminhamento",
        "posicao",
        "prazo",
        "prazo_out",
        'calcular_status',
        'get_data',
        'link_para_reuniao',
        )
    list_filter = (
        "reuniao__politica",
        "reuniao",
        "assunto", 
        "reuniao__data",
        VencimentoProximoFilter,
        "responsavel"
        ) # cria filtros
    list_editable = (
        "prazo_out",
        ) # permite editar do preview
    
    #### modelo com edit ####
    #def link_para_reuniao(self, obj):
    #    url = reverse('admin:reunioes_reuniao_change', args=[obj.reuniao_id])  
    #    return format_html('<a class="button" href="{}">Voltar para Reunião</a>', url)
    #link_para_reuniao.short_description = 'Reunião'

    def link_para_reuniao(self, obj):
        url = reverse('admin:reunioes_reuniao_changelist')  
        url += f'?reuniao_id={obj.reuniao_id}'
        return format_html('<a class="button" href="{}">Voltar para reuniões</a>', url)
    link_para_reuniao.short_description = 'Reunião'

    def get_data(self, obj):
        return obj.reuniao.data
    
    def calcular_status_with_days(self, obj):
        status, dias_restantes, bg_color, text_color, icon_class = obj.calcular_status()
        return format_html(
            '<span style="background-color: {}; color: {};">'
            '<i class="{}"></i> {} ({})'
            '</span>',
            bg_color, text_color, icon_class, status, dias_restantes
        )
    calcular_status_with_days.short_description = 'Status e Dias Restantes'

    get_data.short_description = 'Data'