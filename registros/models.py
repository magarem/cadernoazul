from django.conf import settings
from django.db import models
from django.utils import timezone

class Registro(models.Model):

    #informações do proprietário
    #dono = models.ForeignKey('auth.User')
    dono = models.OneToOneField(settings.AUTH_USER_MODEL)
    grupo = models.ForeignKey("auth.Group")

    #Datas
    data_criado = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)

    # Classificação
    classificacao_ops = (
        (0, 'Normal'),
        (1, 'Atenção'),
        (2, 'Urgente'),
    )
    classificacao = models.IntegerField(choices=classificacao_ops, default=1)

    #Controle de acesso
    visibilidade_ops = (
        (0, '--'),
        (1, 'Apenas leitura'),
        (2, 'Leitura e escrita'),
    )
    # Controle de acesso
    acesso_grupo = models.IntegerField(choices=visibilidade_ops, default=1)
    acesso_outros = models.IntegerField(choices=visibilidade_ops, default=1)
