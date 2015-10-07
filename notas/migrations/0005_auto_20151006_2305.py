# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0004_auto_20151006_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='img',
        ),
        migrations.AddField(
            model_name='nota',
            name='img',
            field=models.ForeignKey(default=1, to='notas.Imagem'),
            preserve_default=False,
        ),
    ]
