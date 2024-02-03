#### BASE ####
from django.db import models
from django.utils.translation import gettext as _
from datetime import date
from django.conf import settings
from django.utils.safestring import mark_safe

#### LIBS ####
from simple_history.models import HistoricalRecords

#### APPS ####
from orgaos.models import Secretaria, Responsavel
from apoio.models import Status

#### modelos ####
class Reuniao(models.Model): # criar reuniões
    politica = models.CharField(_("Política"), max_length=255)
    numero = models.IntegerField(verbose_name = _("Número da reunião"))
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, verbose_name = _("Nome da secretaria"))
    local = models.CharField(_("Local"), max_length=255)
    data = models.DateField(default=date.today, verbose_name = _("Data"))
    hora_inicio = models.TimeField(verbose_name = _("Hora início"))
    hora_termino = models.TimeField(verbose_name = _("Hora término"))
    assunto = models.CharField(_("Assunto"), max_length=255)
    participante = models.ManyToManyField(Responsavel, verbose_name = _("Participante"))

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Reuniões"
    
    def __str__(self):
        return self.politica + " " + str(self.data)

class Encaminhamento(models.Model): # criar reuniões
    # o que
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE, verbose_name = _("Reunião"))
    assunto = models.CharField(_("Assunto"), max_length=255)
    encaminhamento = models.TextField(_("Encaminhamento"))
    # quem
    responsavel = models.ManyToManyField(Responsavel, verbose_name = _("Responsável"))
    gestor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name = _("Nome do(a) Gestor(a)"))
    # quando
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name = _("Status"))
    prazo = models.DateField(default=date.today, verbose_name = _("Prazo Original"))
    prazo_out = models.DateField(default=date.today, verbose_name = _("Novo Prazo"))
    posicao = models.CharField(_("Posição Atual"), max_length=300)
    devolutiva = models.TextField(_("Resposta"))

    history = HistoricalRecords()

    def calcular_status(self):
        dias_restantes = (self.prazo - date.today()).days
        if dias_restantes < 0:
            return 'Atrasado', dias_restantes, 'red', 'white', 'fas fa-exclamation-circle'
        elif dias_restantes == 0:
            return 'Hoje', dias_restantes, 'yellow', 'black', 'fas fa-exclamation-triangle'
        else:
            return 'Em dia', dias_restantes, 'green', 'white', 'fas fa-check-circle'

    class Meta:
        verbose_name_plural = "Encaminhamentos"