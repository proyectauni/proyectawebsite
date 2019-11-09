from django.db import models
class Proyectino(models.Model):
    ApellidoPaterno=models.CharField(max_length=40)
    ApellidoMaterno=models.CharField(max_length=40)
    Nombres=models.CharField(max_length=40)
    DNI=models.CharField(max_length=9)
    FechaNacimiento=models.DateField()
    SEXO=(('f','Femenino'),('M','Masculino'))
    Sexo=models.CharField(max_length=1,choices=SEXO,default='M')

    def NombreCompleto(self):
        cadena="{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)


    def __str__(self):
        return self.NombreCompleto()

class Proyecto(models.Model):
    Nombre=models.CharField(max_length=50)
    Categoría=models.CharField(max_length=50)
    Estado=models.BooleanField(default=True)

    def __str__(self):
        return "{0} {1}".format(self.Nombre, self.Categoría)

class Inscripción(models.Model):
    Alumno=models.ForeignKey(Proyectino, null=False, blank=False, on_delete=models.CASCADE)
    Proyecto=models.ForeignKey(Proyecto, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatrícula=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena="{0}=>{1}"
        return cadena.format(self.Alumno, self.Proyecto)


# Create your models here.
