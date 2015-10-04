# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('data_criado', models.DateTimeField(auto_now_add=True)),
                ('data_alterado', models.DateTimeField(auto_now=True)),
                ('classificacao', models.IntegerField(default=1, choices=[(0, 'Normal'), (1, 'Atenção'), (2, 'Urgente')])),
                ('acesso_grupo', models.IntegerField(default=1, choices=[(0, '--'), (1, 'Apenas leitura'), (2, 'Leitura e escrita')])),
                ('acesso_outros', models.IntegerField(default=1, choices=[(0, '--'), (1, 'Apenas leitura'), (2, 'Leitura e escrita')])),
                ('dono', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('grupo', models.ForeignKey(to='auth.Group')),
            ],
        ),
    ]
