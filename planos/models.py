#### django ####
from django.db import models
from django.forms import ValidationError
from djmoney.models.fields import MoneyField
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator

#### libs ####
from pickle import OBJ
from datetime import date
from simple_history.models import HistoricalRecords
from decimal import Decimal

#### modelos ####
from orgaos.models import Orgao, AIS, Unidade, Responsavel
from apoio.models import Ano, EixoPlano

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

### Plano ###
class Plano(models.Model):
    nome = models.CharField(max_length=255, verbose_name = _("Nome do Plano"))
    
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, verbose_name = _("Ano"))
    mes = models.CharField(max_length=255, choices=mes_lista, verbose_name = _("Mês"))
    
    operativa = models.ForeignKey(Orgao, on_delete=models.CASCADE, verbose_name = _("Nome da Operativa"))
    ais = models.ForeignKey(AIS, on_delete=models.CASCADE, verbose_name = _("Nome da AIS"))
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, verbose_name = _("Nome da Unidade"))

    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, verbose_name = _("Nome do(a) Responsável"))
    gestor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = _("Nome do(a) Gestor(a)"))

    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return str(self.nome)
    
    class Meta:
        verbose_name_plural = "Plano"

### Ação ###
class AcaoPlano(models.Model):
    # what - e traz who e where 3w
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE, verbose_name = _("Plano"))
    # what
    nome = models.CharField(max_length=255, verbose_name = _("Nome da Ação"))
    # how 3w1h
    descricao = models.TextField(blank=True, null=True, verbose_name = _("Descrição"))
    # why 4w1h
    eixo = models.ForeignKey(EixoPlano, on_delete=models.CASCADE, verbose_name = _("Eixo do Plano"))
    # when 5w1h
    data_inicio = models.DateField(default=date.today, verbose_name = _("Início"))
    data_termino = models.DateField(blank=True, null=True, verbose_name = _("Término"))
    # how much 5w2h
    policiais = models.CharField(_("Policiais"), max_length=6, validators=[RegexValidator(r'^\d{1,10}$')])
    diarias = models.CharField(_("Diárias"), max_length=6, validators=[RegexValidator(r'^\d{1,10}$')])
    pjes = models.CharField(_("PJES"), max_length=6, validators=[RegexValidator(r'^\d{1,10}$')])

    history = HistoricalRecords()

    def publish(self):
        self.published_date = date.today()
        self.save()

    def __str__(self):
        return str(self.nome)
    
    class Meta:
        verbose_name_plural = "Ação"