from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from sorl.thumbnail import ImageField, get_thumbnail
from django.conf import settings
from tagging.fields import TagField
from tagging.models import Tag

class Registro(models.Model):
    #informações do proprietário
    #dono = models.ForeignKey('auth.User')

    dono = models.IntegerField(blank=True, null=True)

    #dono = models.OneToOneField(settings.AUTH_USER_MODEL)
    grupo = models.ForeignKey("auth.Group")

    #Datas
    data_criado = models.DateTimeField('date created', blank=True, null=True)
    data_alterado = models.DateTimeField('date updated', blank=True, null=True)

    #Controle de acesso
    visibilidade_ops = (
        (0, '--'),
        (1, 'Apenas leitura'),
        (2, 'Leitura e escrita'),
    )
    # Controle de acesso
    acesso_grupo = models.IntegerField(choices=visibilidade_ops, default=0)
    acesso_outros = models.IntegerField(choices=visibilidade_ops, default=0)

    # Classificação
    classificacao_ops = (
        (0, 'Normal'),
        (1, 'Atenção'),
        (2, 'Urgente'),
    )
    classificacao = models.IntegerField(choices=classificacao_ops, default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            self.data_criado = now()
        self.data_alterado = now()
        super(Registro, self).save(*args, **kwargs)

class Marcador(models.Model):
    #id do registro
    dono = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'marcador'
        verbose_name_plural = 'marcadores'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Nota(Registro):

    #Texto da nota
    texto = models.TextField()
    #imagem de destaque
    imagem = ImageField(blank=True, null=True)
    tags = TagField()
    #marcador = models.ManyToManyField(Marcador)

    def __str__(self):
        return self.texto

    def texto_titulo(self):
        #return self.texto[0:self.texto.find('\n')]
        return self.texto[0:200]

     #Função de geração de miniatura na listagem
    def mini(self):
        if self.imagem:
            t = get_thumbnail(self.imagem,"120x120", quality=100)
            return u'<img src="%s" />' % t.url
        else:
            return u"None"
    mini.short_description = 'Imagem'
    mini.allow_tags = True

    def get_tags(self):
        return Tag.objects.get_for_object(self)

class NotaFile(models.Model):

    nota = models.ForeignKey(Nota, related_name='anexo')
    anexo = models.FileField()

    def __str__(self):
        return ''
