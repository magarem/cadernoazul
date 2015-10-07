# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0009_auto_20151007_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotaFile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('anexo', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='nota',
            name='dono',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notaimage',
            name='nota',
            field=models.ForeignKey(related_name='image', to='notas.Nota'),
        ),
        migrations.AddField(
            model_name='notafile',
            name='nota',
            field=models.ForeignKey(related_name='anexo', to='notas.Nota'),
        ),
    ]
