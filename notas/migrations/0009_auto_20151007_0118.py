# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('notas', '0008_auto_20151007_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notaimage',
            old_name='nota_id',
            new_name='nota',
        ),
        migrations.AddField(
            model_name='nota',
            name='acesso_grupo',
            field=models.IntegerField(choices=[(0, '--'), (1, 'Apenas leitura'), (2, 'Leitura e escrita')], default=0),
        ),
        migrations.AddField(
            model_name='nota',
            name='acesso_outros',
            field=models.IntegerField(choices=[(0, '--'), (1, 'Apenas leitura'), (2, 'Leitura e escrita')], default=0),
        ),
        migrations.AddField(
            model_name='nota',
            name='classificacao',
            field=models.IntegerField(choices=[(0, 'Normal'), (1, 'Atenção'), (2, 'Urgente')], default=0),
        ),
        migrations.AddField(
            model_name='nota',
            name='data_alterado',
            field=models.DateTimeField(blank=True, verbose_name='date updated', null=True),
        ),
        migrations.AddField(
            model_name='nota',
            name='data_criado',
            field=models.DateTimeField(blank=True, verbose_name='date created', null=True),
        ),
        migrations.AddField(
            model_name='nota',
            name='dono',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nota',
            name='grupo',
            field=models.ForeignKey(default=1, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nota',
            name='marcadores',
            field=models.ManyToManyField(blank=True, to='notas.Marcador'),
        ),
    ]
