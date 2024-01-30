from django.db import models
from django.forms import ValidationError
from djmoney.models.fields import MoneyField

from pickle import OBJ
from datetime import date
from django.conf import settings
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.core.validators import RegexValidator
from django.utils.translation import gettext as _

#### apps ####

from apoio.models import Ano, TipoAcao, TipoPrograma

#### utils ####

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

mes_lista = (
    ('1','Jan'),
    ('2','Fev'),
    ('3','Mar'),
    ('4','Abr'),
    ('5','Mai'),
    ('6','Jun'),
    ('7','Jul'),
    ('8','Ago'),
    ('9','Set'),
    ('10','Out'),
    ('11','Nov'),
    ('12','Dez'),
)

def validar_moeda(value):
    if value.amount <= 0:
        raise ValidationError(_("O valor deve ser maior que zero."))
    
#### modelos orçamentários ####
    ########### MODELOS ORÇAMENTÁRIOS ###########
### Fonte ###
class Fontes(models.Model): # fontes das metas
    fonte_cd = models.CharField(_("Código da Fonte"), max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], unique=True)
    fonte_nm = models.CharField(_("Nome da Fonte"), max_length=255)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.fonte_cd
    
    class Meta:
        verbose_name_plural = "Fontes"

### Eixo ###
class Eixo(models.Model): # objetivos estratégicos do governo
    eixo_estrategico = models.CharField(_("Nome do Objetivo"), max_length=255)
    eixo_estrategico_cd = models.CharField(_("Código do Objetivo"), max_length=10, unique=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, verbose_name = _("Ano"))
    descricao = models.TextField(blank=True, null=True, verbose_name = _("Descrição"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.eixo_estrategico + " " + self.eixo_estrategico_cd
    
    class Meta:
        verbose_name = "Objetivo"
        verbose_name_plural = "Objetivo Estratégico"

### Programa ###
class Programa(models.Model):
    eixo_estrategico = models.ForeignKey(Eixo, on_delete=models.CASCADE, verbose_name = _("Nome do Eixo"))
    programa = models.CharField(verbose_name=_("Nome do Programa"), max_length=255)
    programa_cd = models.CharField(_("Código do Programa"), max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], unique=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, verbose_name = _("Ano"))
    
    tipo = models.ForeignKey(TipoPrograma, on_delete=models.CASCADE, verbose_name = _("Tipo"))
    #tipo = models.CharField(max_length=255, blank=True, choices=tipo_programa_lista, verbose_name = _("Tipo"))
    
    descricao = models.TextField(blank=True, verbose_name = _("Descrição"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.programa + " " + self.programa_cd
    
    class Meta:
        verbose_name_plural = "Programa"

### Ação ###
class Acao(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, verbose_name = _("Nome do Programa"))
    acao = models.CharField(max_length=255, verbose_name = _("Nome da Ação"), unique=True)
    acao_cd = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name = _("Código da Ação"), unique=True)
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, verbose_name = _("Ano"))
    
    tipo = models.ForeignKey(TipoAcao, on_delete=models.CASCADE, verbose_name = _("Tipo"))
    #tipo = models.CharField(max_length=255, blank=True, choices=tipo_acao_lista, verbose_name = _("Tipo"))
    
    descricao = models.TextField(blank=True, verbose_name = _("Descrição"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.acao + " " + self.acao_cd
    
    class Meta:
        verbose_name_plural = "Ação"