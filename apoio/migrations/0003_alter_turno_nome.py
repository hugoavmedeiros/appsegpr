# Generated by Django 4.2.4 on 2024-01-31 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoio', '0002_municipio_turno_bairro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome do Turno'),
        ),
    ]