from django.shortcuts import render
from django.http import HttpResponse

from app.models import Equipo, Jugador

from app import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def index(request):
    return HttpResponse('<h1>Hola mundo Django! 23525!🦄</h1>')

@api_view(['GET']) 
def get_equipos(request):
    """
    Lista todos las peliculas
    """
    #se buscan todos los registros guardados en la base
    equipos = Equipo.objects.all() #SELECT * FROM app_movie
    #cuando estás serializando múltiples instancias de un modelo
    serializer = serializers.EquipoSerializer(equipos, many=True)
    #Response es una clase que me permite devolver una respuesta
    #que cumple con los estandares de API-REST
    return Response(serializer.data)

@api_view(['POST'])
def create_equipo(request):
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

@api_view(['GET'])
def get_equipo(request, id):
    """
    Muestra una Equipo.
    """
    try:
        #Se busca la pelicula en base por el id
        equipo = Equipo.objects.get(pk=id)        
    except Equipo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')

    serializer = serializers.EquipoSerializer(equipo)
    return Response(serializer.data)

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



# def delete_equipo(request):
#     return HttpResponse('<h2>Se borra la equipo</h2>')



