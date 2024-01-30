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
    
#### modelos orçamentários ####
    
############ MODELOS CONTEXTUAIS ############
### Secretaria ###
class Secretaria(models.Model):
    nome = models.CharField(max_length=255, verbose_name = _("Nome da Secretaria"))
    sigla = models.CharField(max_length=10, verbose_name = _("Sigla da Secretaria"))
    codigo = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name = _("Código da Secretaria"), unique=True)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.nome + " " + self.sigla
    
    class Meta:
        verbose_name_plural = "Secretaria"

### Órgão ###
class Orgao(models.Model):
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, verbose_name = _("Nome da Secretaria"))
    nome = models.CharField(max_length=255, verbose_name = _("Nome do Órgão"))
    sigla = models.CharField(max_length=10, verbose_name = _("Sigla do Órgão"))
    codigo = models.CharField(max_length=10, blank=True, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name = _("Código do Órgão"), unique=True)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Órgão"   

### AIS ###
class AIS(models.Model):
    nome = models.CharField(max_length=255, verbose_name = _("Nome da AIS"))
    sigla = models.CharField(max_length=5, verbose_name = _("Sigla da AIS"))
    codigo = models.CharField(max_length=2, blank=True, validators=[RegexValidator(r'^\d{1,10}$')], verbose_name = _("Código da AIS"), unique=True)
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.sigla
    
    class Meta:
        verbose_name_plural = "AIS"

### Unidade ###
class Unidade(models.Model):
    orgao = models.ForeignKey(
        Orgao, 
        on_delete=models.CASCADE, 
        verbose_name = _("Nome da Operativa")
        )
    nome = models.CharField(max_length=255, verbose_name = _("Nome da Unidade"))
    sigla = models.CharField(max_length=5, verbose_name = _("Sigla da Unidade"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.sigla
    
    class Meta:
        verbose_name_plural = "AIS"

### Responsável ###
class Responsavel(models.Model):
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, verbose_name = _("Nome da Secretaria"))
    orgao = models.ForeignKey(Orgao, on_delete=models.CASCADE, blank=True, null=True, verbose_name = _("Nome do Órgão"))
    nome = models.CharField(max_length=255, verbose_name = _("Nome do(a) Responsável"))
    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Responsável"   