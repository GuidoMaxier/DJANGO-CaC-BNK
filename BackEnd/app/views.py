from django.shortcuts import render
from django.http import HttpResponse

from app.models import Equipo, Jugador

from app import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def index(request):
    return HttpResponse('<h1>Estas en el prefijo de la API</h1>')


### CRUD EQUIPO ####
@api_view(['GET']) 
def get_equipos(request):
    """
    Lista todos los equipos.
    """
    #se buscan todos los registros guardados en la base
    equipos = Equipo.objects.all() 
    #cuando estás serializando múltiples instancias de un modelo
    serializer = serializers.EquipoSerializer(equipos, many=True)
    #Response es una clase que me permite devolver una respuesta
    #que cumple con los estandares de API-REST
    return Response(serializer.data)


@api_view(['GET'])
def get_equipo(request, id):
    """
    Muestra un Equipo por id.
    """
    try:
        #Se busca el equipo por id
        equipo = Equipo.objects.get(pk=id)        
    except Equipo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')

    serializer = serializers.EquipoSerializer(equipo)
    return Response(serializer.data)


@api_view(['POST'])
def create_equipo(request):
    """
    Crea un Equipo.
    """
    #Se seriala los datos recibidos desde el formulario
    serializer = serializers.EquipoSerializer(data=request.data)
    #Se ejecutan las validaciones
    if serializer.is_valid():
        #Se registra en base de datos
        serializer.save()
        #Se genera la respuesta que deseamos devolver
        response = {'status':'Ok',
                    'message':'Equipo CREADO correctamente',
                    'data':serializer.data}
        return Response(data= response, status=status.HTTP_201_CREATED)
    
    response = {'status':'Error',
                'message':'No se pudo CREAR el equipo',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_equipo(request, id):
    """
    Actualiza una equipo.
    """
    try:
        equipo = Equipo.objects.get(pk=id)
    except Equipo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    
    serializer = serializers.EquipoSerializer(equipo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status':'Ok',
                    'message':'Equipo modificado exitosamente',
                    'data':serializer.data}
        return Response(data=response)
    response = {'status':'Error',
                'message':'No se pudo modificar equipo',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_equipo(request, id):
    """
    Eliminar un equipo.
    """
    try:
        equipo = Equipo.objects.get(pk=id)        
    except Equipo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    #Se elimina la pelicula en base de datos
    equipo.delete()
    return Response({'message':'Se elimino el Equipo'},status=status.HTTP_200_OK)



##### CRUD DE JUGADOR #####

@api_view(['GET'])
def get_jugadores(request):
    """
    Muestra todos los Jugadores.
    """
    jugadores = Jugador.objects.all()
    serializer = serializers.JugadorSerializer(jugadores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_jugador(request, id):
    """
    Muestra un jugador por id.
    """
    try:
        jugador = Jugador.objects.get(pk=id)
    except Jugador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Recurso no encontrado')

    serializer = serializers.JugadorSerializer(jugador)
    return Response(serializer.data)


@api_view(['POST'])
def create_jugador(request):
    """
    Crea un Jugador.
    """
    serializer = serializers.JugadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status': 'Ok', 'message': 'Jugador creado correctamente', 'data': serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {'status': 'Error', 'message': 'No se pudo crear el jugador', 'errors': serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_jugador(request, id):
    """
    Actuliza un Jugador.
    """
    try:
        jugador = Jugador.objects.get(pk=id)
    except Jugador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Recurso no encontrado')

    serializer = serializers.JugadorSerializer(jugador, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status': 'Ok', 'message': 'Jugador modificado exitosamente', 'data': serializer.data}
        return Response(data=response)

    response = {'status': 'Error', 'message': 'No se pudo modificar el jugador', 'errors': serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_jugador(request, id):
    """
    Elimina un Jugador
    """
    try:
        jugador = Jugador.objects.get(pk=id)
    except Jugador.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Recurso no encontrado')

    jugador.delete()
    return Response({'message': 'Jugador eliminado'}, status=status.HTTP_200_OK)


##### EQUIPO Y JUGADOR #####
@api_view(['GET'])
def get_equipo_detalles(request, nombre_equipo):
    try:
        equipo = Equipo.objects.get(nombre=nombre_equipo)
    except Equipo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Equipo no encontrado')

    # Serializar datos del equipo
    equipo_serializer = serializers.EquipoSerializer(equipo)

    # Obtener todos los jugadores del equipo
    jugadores = Jugador.objects.filter(equipo=equipo)
    jugadores_serializer = serializers.JugadorSerializer(jugadores, many=True)

    # Construir la respuesta combinada
    respuesta = {
        'equipo': equipo_serializer.data,
        'jugadores': jugadores_serializer.data
    }

    return Response(respuesta)








