# Generated by Django 4.2.4 on 2024-01-31 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apoio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Município')),
                ('codigo', models.CharField(max_length=7, verbose_name='Código do Município')),
                ('rd', models.CharField(default='-', max_length=30, verbose_name='Região de Desenvolvimento')),
            ],
            options={
                'verbose_name_plural': 'Município',
                'permissions': [('can_export_data', 'Can Export Data')],
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Bairro')),
            ],
            options={
                'verbose_name_plural': 'Turno',
            },
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Bairro')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apoio.municipio', verbose_name='Nome Município')),
            ],
            options={
                'verbose_name_plural': 'Bairro',
                'permissions': [('can_export_data', 'Can Export Data')],
            },
        ),
    ]