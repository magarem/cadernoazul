# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
        ('notas', '0002_auto_20151005_0247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='dono',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='reg',
        ),
        migrations.AddField(
            model_name='nota',
            name='acesso_grupo',
            field=models.IntegerField(default=0, choices=[(0, '--'), (1, 'Apenas leitura'), (2, 'Leitura e escrita')]),
        ),
        migrations.AddField(
            model_name='nota',
            name='acesso_outros',
            field=models.IntegerField(default=0, choices=[(0, '--'), (1, 'Apenas leitura'), (2, 'Leitura e escrita')]),
        ),
        migrations.AddField(
            model_name='nota',
            name='data_alterado',
            field=models.DateTimeField(null=True, blank=True, verbose_name='date updated'),
        ),
        migrations.AddField(
            model_name='nota',
            name='data_criado',
            field=models.DateTimeField(null=True, blank=True, verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='nota',
            name='dono',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, verbose_name='Dono'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nota',
            name='grupo',
            field=models.ForeignKey(default=1, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Registro',
        ),
    ]
