from django.db import models

# Create your models here.

class Persona(models.Model):
    #Si se quiere crear un atributo que sea la clave primaria se crearía de la siguiente:
    #rut = models.CharField(primary_key=True), de omitir algo como éstó, django lo crea solo
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, null=True,blank=True)
    numero_mascotas = models.IntegerField()
    razones = models.TextField()