# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('img', models.ImageField(blank=True, upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Marcador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': 'marcador',
                'verbose_name_plural': 'marcadores',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('texto', models.TextField()),
                ('img', models.ManyToManyField(to='notas.Imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('data_criado', models.DateTimeField(verbose_name='date created')),
                ('data_alterado', models.DateTimeField(verbose_name='date updated')),
                ('classificacao', models.IntegerField(choices=[(0, 'Normal'), (1, 'Atenção'), (2, 'Urgente')], default=0)),
                ('acesso_grupo', models.IntegerField(choices=[(0, '--'), (1, 'Apenas leitura'), (2, 'Leitura e escrita')], default=0)),
                ('acesso_outros', models.IntegerField(choices=[(0, '--'), (1, 'Apenas leitura'), (2, 'Leitura e escrita')], default=0)),
                ('dono', models.ForeignKey(verbose_name='Dono', to=settings.AUTH_USER_MODEL)),
                ('grupo', models.ForeignKey(to='auth.Group')),
                ('marcadores', models.ManyToManyField(to='notas.Marcador', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='nota',
            name='reg',
            field=models.OneToOneField(to='notas.Registro'),
        ),
    ]
