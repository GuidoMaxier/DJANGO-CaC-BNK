// Para el Entorno Virtual
pip install virtualenv
virtualenv venv
source venv/Scripts/activate

// para instalar facil y rapido
pip install -r requirements.txt

// Instalacion Django 4.2.7
pip install Django==4.2.7

// para lista aplicaciones instaladas
pip freeze 

// Para crear el Proyecto
django-admin startproject "nombre proyecto"

// abrir con el VS code (en la carta del proyecto)
code .

// crear APP
python manage.py startapp app

//clase 32
// creamos el archivo urls.py en la carpeta "app"
from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index, name='inicio_app'),
    path('get_movies/', views.get_movies, name='get_app'),
]

// y modificamos el archivo urls de Django

urls django
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
]


// MySQL + Pillow
pip install mysql
pip install pillow

pip freeze > requirements.txt


// Configuramos Setting para Mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TORNEOS',
        'USER': 'Guido_Maxier',
        'PASSWORD': 'miclave',
        'HOST': 'localhost',
        'PORT': 3306,

    }
}


// cambiar MySQL (dejar sin clave)
ALTER USER 'root'@'localhost' IDENTIFIED BY '';
FLUSH PRIVILEGES;


// Variable de Entorno .env
pip install django-environ


-------------.env-----------------------
SECRET_KEY=django-insecure-rno9ax%@c+c3644ipz336_w)_)(*woy$^$j9pb6z5*oqi4nv

DATABASE_NAME=torneos
DATABASE_USER=root
DATABASE_PASSWORD=
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
----------------------------------------
//codigo para agregar en setting

import os
import environ

env = environ.Env()
environ.Env.read_env()

----------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),

    }
}
---------------------------------------------
// CREAR ARCHIVO .env.example para compartir la estructuta de .env

//CREAR EL gitignore
gitignore.io
https://www.toptal.com/developers/gitignore/

// inicio git
git init
git add .
git commit -m "Primer subida"

// comenzamos con los modelos

--------------------------------------
class Movie(models.Model):
    
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=100)
    release_date = models.DateField(null=True)

------------------------------------------
// para crear las tabla del modelo
python manage.py makemigrations   //crea las migraciones
python manage.py migrate       //creas las tablas


//agremos esta lineas en setting para la carpeta media
#donde vamos a ir guardar los archivos medias debug
MEDIA_URL = "/media/"
#media para produccion
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
la carpeta media esta en la raiz a la altura de app

// en el urls.py agregamos
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 


//Para la API REST




