from django.db import models
from app.proyectino.models import Proyectino
# Create your models here.

class Tipo(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()

class Documento(models.Model):
    nombre_carpeta = models.CharField(max_length = 100)
    link_drive = models.URLField(blank = False)
    autor = models.ForeignKey(Proyectino, on_delete=models.CASCADE)
    fecha_subida = models.DateField(auto_now_add=True)
    
class Proyecto(models.Model):
    name = models.CharField(max_length=75)
    logo = models.ImageField(upload_to = 'proyecto/logo', blank = True, null = True)
    descripcion = models.TextField()
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(blank=True)
    fecha_fin = models.DateField(blank=True)
    # aliados = models.ForeignKey() relacion requerida
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

class ProyectoProyectino (models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    proyectino = models.ForeignKey(Proyectino, on_delete=models.CASCADE)
    rol = models.CharField(max_length = 50)
    fecha_ingreso = models.DateField(help_text = 'fecha en la que ingreso el proyectino al proyecto') 
    fecha_salida = models.DateField(help_text = 'fecha en la que salio el proyectino del proyecto')