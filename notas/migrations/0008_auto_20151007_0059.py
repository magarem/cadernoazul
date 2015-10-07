# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0007_auto_20151007_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='acesso_grupo',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='acesso_outros',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='classificacao',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='data_alterado',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='data_criado',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='dono',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='marcadores',
        ),
    ]
