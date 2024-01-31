#### BASE ####
from django.db import models
from django.utils.translation import gettext as _
from datetime import date
from django.conf import settings

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
    prazo = models.DateField(default=date.today, verbose_name = _("Prazo"))
    devolutiva = models.TextField(_("Devolutiva"))

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Encaminhamentos"