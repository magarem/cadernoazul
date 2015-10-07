# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0003_auto_20151006_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='dono',
            field=models.IntegerField(),
        ),
    ]
