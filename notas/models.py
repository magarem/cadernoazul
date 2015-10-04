from django.db import models
from django.utils import timezone

class Nota(models.Model):

    #id do registro
    registro = models.OneToOneField('registros.Registro')

    #Texto da nota
    texto = models.TextField()

    def __str__(self):
        return self.texto
