
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio_app'),


    ### DEPORTE ###
    path('create_deporte/', views.create_deporte, name='create_deporte_app'), 
    path('deportes/', views.get_deportes, name='get_deportes_app'), 

    ### EQUIPOS ###
    path('equipos/', views.get_equipos, name='get_equipos_app'), #OK
    path('equipo/<int:id>/', views.get_equipo, name='get_equipo'), #OK

    path('create_equipo/', views.create_equipo, name='create_equipo_app'), 
    path('update_equipo/<int:id>/', views.update_equipo, name='update_equipo_app'),
    path('delete_equipo/<int:id>/', views.delete_equipo, name='delete_equipo_app'),


    ### JUGADOR ###
    path('jugadores/', views.get_jugadores, name='get_jugadores_app'),
    path('jugador/<int:id>/', views.get_jugador, name='get_jugador_app'),

    path('create_jugador', views.create_jugador, name='create_jugador_app'),
    path('update_jugador/<int:id>/', views.update_jugador, name='update_jugador_app'),
    path('delete_jugador/<int:id>/', views.delete_jugador, name='delete_jugador_app'),
    

    ### EQUIPO Y JUGADOR ###
    path('equipos_detalles/<str:nombre_equipo>/', views.get_equipo_detalles, name='get_equipo_detalles_app'),

]


 