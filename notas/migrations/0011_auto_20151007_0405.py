# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0010_auto_20151007_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notaimage',
            name='nota',
        ),
        migrations.AddField(
            model_name='nota',
            name='imagem',
            field=models.ImageField(upload_to='', default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NotaImage',
        ),
    ]
