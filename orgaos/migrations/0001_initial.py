# Generated by Django 4.2.4 on 2024-02-02 19:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AIS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da AIS')),
                ('sigla', models.CharField(max_length=5, verbose_name='Sigla da AIS')),
                ('codigo', models.CharField(blank=True, max_length=2, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da AIS')),
            ],
            options={
                'verbose_name_plural': 'AIS',
            },
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Órgão')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla do Órgão')),
                ('codigo', models.CharField(blank=True, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Órgão')),
            ],
            options={
                'verbose_name_plural': 'Órgão',
            },
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Secretaria')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla da Secretaria')),
                ('codigo', models.CharField(blank=True, max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Secretaria')),
            ],
            options={
                'verbose_name_plural': 'Secretaria',
            },
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Unidade')),
                ('sigla', models.CharField(max_length=5, verbose_name='Sigla da Unidade')),
                ('orgao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgaos.orgao', verbose_name='Nome da Operativa')),
            ],
            options={
                'verbose_name_plural': 'Unidade',
            },
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do(a) Responsável')),
                ('orgao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orgaos.orgao', verbose_name='Nome do Órgão')),
                ('secretaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgaos.secretaria', verbose_name='Nome da Secretaria')),
            ],
            options={
                'verbose_name_plural': 'Responsável',
            },
        ),
        migrations.AddField(
            model_name='orgao',
            name='secretaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgaos.secretaria', verbose_name='Nome da Secretaria'),
        ),
        migrations.CreateModel(
            name='HistoricalUnidade',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Unidade')),
                ('sigla', models.CharField(max_length=5, verbose_name='Sigla da Unidade')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('orgao', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orgaos.orgao', verbose_name='Nome da Operativa')),
            ],
            options={
                'verbose_name': 'historical unidade',
                'verbose_name_plural': 'historical Unidade',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSecretaria',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da Secretaria')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla da Secretaria')),
                ('codigo', models.CharField(blank=True, db_index=True, max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da Secretaria')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical secretaria',
                'verbose_name_plural': 'historical Secretaria',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalResponsavel',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do(a) Responsável')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('orgao', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orgaos.orgao', verbose_name='Nome do Órgão')),
                ('secretaria', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orgaos.secretaria', verbose_name='Nome da Secretaria')),
            ],
            options={
                'verbose_name': 'historical responsavel',
                'verbose_name_plural': 'historical Responsável',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalOrgao',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Órgão')),
                ('sigla', models.CharField(max_length=10, verbose_name='Sigla do Órgão')),
                ('codigo', models.CharField(blank=True, db_index=True, max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código do Órgão')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('secretaria', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='orgaos.secretaria', verbose_name='Nome da Secretaria')),
            ],
            options={
                'verbose_name': 'historical orgao',
                'verbose_name_plural': 'historical Órgão',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAIS',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome da AIS')),
                ('sigla', models.CharField(max_length=5, verbose_name='Sigla da AIS')),
                ('codigo', models.CharField(blank=True, db_index=True, max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Código da AIS')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ais',
                'verbose_name_plural': 'historical AIS',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
