# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0005_auto_20151006_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotaImage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='nota',
            name='img',
        ),
        migrations.DeleteModel(
            name='Imagem',
        ),
        migrations.AddField(
            model_name='notaimage',
            name='nota',
            field=models.ForeignKey(to='notas.Nota', related_name='images'),
        ),
    ]
