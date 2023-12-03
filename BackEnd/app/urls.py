
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio_app'),
    path('get_equipos/', views.get_equipos, name='get_app'),
]


# urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import EquipoViewSet, JugadorViewSet

# router = DefaultRouter()
# router.register(r'equipos', EquipoViewSet)
# router.register(r'jugadores', JugadorViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]
