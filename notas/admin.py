from django.contrib import admin
from .models import Registro, Nota, NotaFile, Marcador
from django.db.models import Q
from sorl.thumbnail.admin import AdminImageMixin
from django.utils.html import format_html

class preAdmin():

    def save_model(self, request, obj, form, change):

        if obj.data_criado is None:
           obj.dono = request.user.id
           #obj.dono_nome = request.user.username
           #obj.grupo = request.user.groups.all()[0].id
           #obj.grupo = 1
           obj.save()
        else:
           obj.save()
           #obj.user = request.user.id
           #obj.grupo = request.user.groups.all()files

    def get_queryset(self, request):
        qs = super(preAdmin, self).get_queryset(request)

        if request.user.is_superuser:
           return qs

        return qs.filter(Q(dono=request.user.id) | (Q(acesso_grupo__in=[2,3]) & Q(grupo__in = request.user.groups.all())))


#class NotaAdmin(preAdmin, admin.ModelAdmin):
#    pass

class NotaFileInline(admin.TabularInline):

    model = NotaFile
    extra = 1


class NotaAdmin(preAdmin, admin.ModelAdmin):


    def classi(self, obj):
        if (obj.classificacao == 0):
            return format_html('<span style="color: green;"><b>Normal</b></span>')
        if (obj.classificacao == 1):
            return format_html('<span style="color: #FFBF00;"><b>Atenção</b></span>')
        if (obj.classificacao == 2):
            return format_html('<span style="color: red;"><b>Urgente!</b></span>')


    classi.allow_tags = True
    classi.admin_order_field = 'classificacao'
    classi.short_description = 'Classificação'

    #list_display = ('texto_titulo', 'thumb', 'data_criado', 'data_alterado', 'classificacao')
    list_display = ('texto_titulo', 'mini', 'get_data_criado', 'classi')
    inlines = [NotaFileInline]

    def get_data_criado(self, obj):
            return obj.data_criado
    get_data_criado.short_description = 'Criado'
    get_data_criado.admin_order_field = 'data_criado'


    def get_marcadores(self, obj):
            return obj.marcadores.all()
    get_marcadores.short_description = 'Criado'
    get_marcadores.admin_order_field = 'data_criado'


# Register your models here.
admin.site.register(Nota, NotaAdmin)
admin.site.register(Marcador)
