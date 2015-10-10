from django.contrib import admin
from .models import Registro, Nota, NotaFile, Marcador
from django.db.models import Q
from sorl.thumbnail.admin import AdminImageMixin
from django.utils.html import format_html

class PreMarcador(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.dono = request.user.id
        obj.save()

    def get_queryset(self, request):
        qs = super(PreMarcador, self).get_queryset(request)
        if request.user.is_superuser:
           return qs

        return qs.filter(dono=request.user.id)


class PreAdmin(AdminImageMixin):

    def save_model(self, request, obj, form, change):

        if obj.data_criado is None:
           obj.dono = request.user.id
           obj.save()
        else:
           obj.save()

    def get_queryset(self, request):
        qs = super(PreAdmin, self).get_queryset(request)

        if request.user.is_superuser:
           return qs

        return qs.filter(Q(dono=request.user.id) | (Q(acesso_grupo__in=[2,3]) & Q(grupo__in = request.user.groups.all())))

class NotaFileInline(admin.TabularInline):

    model = NotaFile
    extra = 1


class NotaAdmin(PreAdmin, admin.ModelAdmin):

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
    inlines = [NotaFileInline, ]

    fieldsets = (
            ('Texto', {
                'classes': ('collapse',),
                'fields': ('texto', 'classificacao', 'tags')
            }),
            ('Imagem e Anexos', {
                'classes': ('collapse',),
                'fields': ('imagem',)
            }),
            ('Controle', {
                'classes': ('collapse',),
                'fields': ('dono', 'grupo', 'acesso_grupo', 'acesso_outros')
            }),

        )

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
admin.site.register(Marcador, PreMarcador)
