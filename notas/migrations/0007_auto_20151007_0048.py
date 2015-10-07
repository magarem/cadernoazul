# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0006_auto_20151006_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notaimage',
            old_name='nota',
            new_name='nota_id',
        ),
    ]
