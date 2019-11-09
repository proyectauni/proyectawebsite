from django.db import models

# Create your models here.

class Especialidad(models.Model):
    nombre_esp = models.CharField(max_length=30)
    nombre_facu = models.CharField(max_length=75, help_text="aquí irá el nombre completo de la facultad y no de forma abreviada")
    abreviaura = models.CharField(max_length=10, help_text="aquí irá las siglas de la facu")

class Proyectino(models.Model):
    name = models.CharField(max_length=75)
    lastname = models.CharField(max_length=75)
    email = models.EmailField(max_length=75)
    celular = models.CharField(max_length=20)
    fecha_ingreso = models.DateField(blank=True)
    fecha_nacimiento = models.DateField(blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    dni = models.CharField(max_length=10)
    cod_uni = models.CharField(max_length=10, help_text="este será el código de la uni de cada estudiante")
    estado = models.CharField(help_text="indica el estado activo/inactivo/honoraio.. de un miembro",max_length=75)
    cantidad_toribonus = models.IntegerField()

class Certificacion_proyectino(models.Model):
    proyectino = models.ForeignKey(Proyectino, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=75)
    fecha_certificación = models.CharField(max_length=75)

class Tipo_toribonu(models.Model):
    descripcion = models.CharField(max_length = 75)

class Toribonu(models.Model):
    emisor = models.CharField(max_length=75, help_text="nombre de la persona que está asignando los toribonus")
    proyectino = models.ForeignKey(Proyectino, on_delete=models.CASCADE)
    tipo_toribonu = models.ForeignKey(Tipo_toribonu, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=75)
    cantidad = models.IntegerField()