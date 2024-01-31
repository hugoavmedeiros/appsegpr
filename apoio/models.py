from django.db import models
from django.forms import ValidationError
from djmoney.models.fields import MoneyField

# Create your models here.
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

from django.db import models

### Eixo do Plano ###
class EixoPlano(models.Model): # lista com tipos de metas
    nome = models.CharField(_("Tipo"), max_length=255)
    descricao = models.TextField(blank=True, null=True, verbose_name = _("Descrição"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Eixo do Plano"

### Ano ###
class Ano(models.Model): # lista com ano
    ano_nr = models.IntegerField(
        verbose_name = _("Ano"),
        default = 2024
        )
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return str(self.ano_nr)
    
    class Meta:
        verbose_name_plural = "Ano"

class TipoPrograma(models.Model): # lista com tipos de programa
    tipo_programa_nm = models.CharField(_("Tipo"), max_length=255)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.tipo_programa_nm
    
    class Meta:
        verbose_name_plural = "Tipo do Programa"

### Tipo de Ação ###
class TipoAcao(models.Model): # lista com tipos de ação
    tipo_acao_nm = models.CharField(_("Tipo"), max_length=255)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.tipo_acao_nm
    
    class Meta:
        verbose_name_plural = "Tipo da Ação"

### Indicador ###
class Indicador(models.Model): # lista com tipos de metas
    nome = models.CharField(_("Tipo"), max_length=255)
    sigla = models.CharField(_("Tipo"), max_length=255)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.sigla
    
    class Meta:
        verbose_name_plural = "Indicador"

### Município ###
class Municipio(models.Model):
    nome = models.CharField(max_length=100, verbose_name = _("Nome do Município"))
    codigo = models.CharField(max_length=7, verbose_name = _("Código do Município"))
    rd = models.CharField(max_length=30, verbose_name = _("Região de Desenvolvimento"), default="-")

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Município"
        permissions = [("can_export_data", "Can Export Data")]

### Bairro ###
class Bairro(models.Model):
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, verbose_name = _("Nome Município"))
    nome = models.CharField(max_length=100, verbose_name = _("Nome do Bairro"))

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Bairro"
        permissions = [("can_export_data", "Can Export Data")]

### Turno ###
class Turno(models.Model):
    nome = models.CharField(max_length=100, verbose_name = _("Nome do Turno"))

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Turno"

### Status ###
class Status(models.Model): # lista com status de metas e etapas
    nome = models.CharField(_("Status"), max_length=255)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Status"