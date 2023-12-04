from rest_framework import serializers
from app.models import Deporte, Equipo, Jugador

class DeporteSerializer(serializers.ModelSerializer):
   
    class Meta:
        #Hacemos correspondencia del serializador con la el modelo
        model = Deporte
        fields = ['id','nombre']

class EquipoSerializer(serializers.ModelSerializer):
   
    class Meta:
        #Hacemos correspondencia del serializador con la el modelo
        model = Equipo
        fields = ['id','nombre', 'logo', 'deporte']

class JugadorSerializer(serializers.ModelSerializer):
   
    class Meta:
        #Hacemos correspondencia del serializador con la el modelo
        model = Jugador
        fields = ['id','nombre', 'fecha_nacimiento', 'dni', 'equipo']                