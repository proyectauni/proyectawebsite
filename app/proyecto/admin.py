from django.contrib import admin
from .models import *
# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('name', 'tipo', 'fecha_inicio', 'fecha_fin', 'documento',)
    list_filter = ('tipo','fecha_inicio','fecha_fin',)
    search_fields = ('name',)
    ordering = ('name','fecha_inicio')

class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo','descripcion',)
    list_filter = ('tipo',)
    search_fields = ('tipo',)
    ordering = ('tipo',)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_carpeta', 'autor', 'fecha_subida',)
    list_filter = ('nombre_carpeta', 'autor', 'fecha_subida',)
    search_fields = ('nombre_carpeta', 'autor',)
    ordering = ('nombre_carpeta', 'autor', 'fecha_subida',)

class ProyectoProyectinoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'proyectino','rol','fecha_ingreso','fecha_salida',)
    list_filter = ('proyecto', 'proyectino','rol','fecha_ingreso','fecha_salida',)
    search_fields = ('proyecto', 'proyectino',)
    ordering = ('proyecto', 'proyectino','rol','fecha_ingreso','fecha_salida',)

admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Documento,DocumentoAdmin)
admin.site.register(ProyectoProyectino,ProyectoProyectinoAdmin)