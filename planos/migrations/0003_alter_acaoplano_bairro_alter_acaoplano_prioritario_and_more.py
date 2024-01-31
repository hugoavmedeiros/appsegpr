# Generated by Django 4.2.4 on 2024-01-31 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoio', '0003_alter_turno_nome'),
        ('planos', '0002_acaoplano_bairro_acaoplano_municipio_acaoplano_turno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acaoplano',
            name='bairro',
            field=models.ManyToManyField(to='apoio.bairro', verbose_name='Nome do Bairro'),
        ),
        migrations.AlterField(
            model_name='acaoplano',
            name='prioritario',
            field=models.BooleanField(default=False, verbose_name='Território Prioritário?'),
        ),
        migrations.AlterField(
            model_name='historicalacaoplano',
            name='prioritario',
            field=models.BooleanField(default=False, verbose_name='Território Prioritário?'),
        ),
    ]