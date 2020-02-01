from django.db import models

# Create your models here.

class Sponsor(models.Model):
    imagen = models.ImageField(upload_to = 'landing/sponsor', blank = True, null = True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + ' || ' + str(self.estado)

class Revista(models.Model):
    year = models.CharField(max_length=75)
    link = models.URLField(blank = False)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.year

class Message(models.Model):
    date_register = models.DateTimeField(auto_now=True, blank=True)
    user_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)
    message = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, default="")

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return str(self.pk)


