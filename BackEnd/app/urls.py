
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio_app'),
    path('equipos/', views.get_equipos, name='get_equipos_app'),
    path('create_equipo/', views.create_equipo,name='create_equipo_app'),
    path('delete_equipo/', views.delete_equipo,name='delete_equipo_app'),
]

