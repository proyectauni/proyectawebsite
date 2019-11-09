from django.contrib import admin
from .models import *

# Register your models here.

class Certificacion_proyectinoInLine(admin.TabularInline):
    model = Certificacion_proyectino

class ProyectinoAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'email', 'celular', 'fecha_ingreso', 'fecha_nacimiento', 'cantidad_toribonus', 'estado')
    list_filter = ('estado',)
    search_fields = ('name','lastname')
    ordering = ('name','lastname')
    inlines = [Certificacion_proyectinoInLine]

admin.site.register(Proyectino, ProyectinoAdmin)
admin.site.register(Especialidad)
admin.site.register(Tipo_toribonu)
admin.site.register(Toribonu)