# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registro',
            name='classificacao',
        ),
        migrations.RemoveField(
            model_name='registro',
            name='marcadores',
        ),
        migrations.AddField(
            model_name='nota',
            name='classificacao',
            field=models.IntegerField(default=0, choices=[(0, 'Normal'), (1, 'Atenção'), (2, 'Urgente')]),
        ),
        migrations.AddField(
            model_name='nota',
            name='marcadores',
            field=models.ManyToManyField(blank=True, to='notas.Marcador'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='data_alterado',
            field=models.DateTimeField(blank=True, verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='data_criado',
            field=models.DateTimeField(blank=True, verbose_name='date created'),
        ),
    ]
