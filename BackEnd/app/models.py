from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=255)

class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='imagenes/', null=True, verbose_name='Logo')
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    # Agrega otros campos necesarios para un jugador

