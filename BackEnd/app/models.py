from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

class Equipo(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Logo')
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
 
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    dni = models.IntegerField(unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nombre

