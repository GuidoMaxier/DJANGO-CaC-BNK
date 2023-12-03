from django.shortcuts import render
from django.http import HttpResponse

# views.py
from rest_framework import viewsets
from .models import Equipo, Jugador
from .serializers import EquipoSerializer, JugadorSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
