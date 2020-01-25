from django.contrib import admin
from .models import *

# Register your models here.

class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('nombre_esp', 'nombre_facu', 'abreviaura')
    list_filter = ('nombre_esp', 'nombre_facu', 'abreviaura')
    search_fields = ('nombre_esp', 'nombre_facu', 'abreviaura')
    ordering = ('nombre_esp', 'nombre_facu', 'abreviaura')

class Certificacion_proyectinoInLine(admin.TabularInline):
    model = Certificacion_proyectino

class ProyectinoAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'celular', 'fecha_ingreso', 'fecha_nacimiento', 'cantidad_toribonus', 'estado')
    list_filter = ('estado',)
    search_fields = ('name','lastname')
    ordering = ('name','lastname')
    inlines = [Certificacion_proyectinoInLine]

class DirectivaAdmin(admin.ModelAdmin):
    list_display = ('gerente', 'cargo', 'periodo')
    list_filter = ('gerente', 'cargo', 'periodo')
    search_fields = ('gerente', 'cargo', 'periodo')
    ordering = ('gerente', 'cargo', 'periodo')

class ToribonuAdmin(admin.ModelAdmin):
    list_display = ('emisor', 'proyectino')
    list_filter = ('emisor', 'proyectino')
    search_fields = ('emisor', 'proyectino')
    ordering = ('emisor', 'proyectino')


class Tipo_toribonuAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)
    list_filter = ('descripcion',)
    search_fields = ('descripcion',)
    ordering = ('descripcion',)

admin.site.register(Proyectino, ProyectinoAdmin)
admin.site.register(Directiva, DirectivaAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Tipo_toribonu, Tipo_toribonuAdmin)
admin.site.register(Toribonu, ToribonuAdmin)