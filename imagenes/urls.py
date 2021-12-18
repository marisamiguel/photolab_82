from django.conf import settings

from django.urls import path
from imagenes.views import *
from . import views



urlpatterns = [
    path('',views.imagenes,name="home"),

    path('imagenes',views.imagenes,name="imagenes"),
    #listar imagenes
    path('listar', views.ImagenesListView.as_view(), 
        name='Listado de Imagenes'),
    #crear imagenes
    path('crear', views.ImagenCreateView.as_view(),
        name="creaimagen" ),
        #borrar
    path('borrar/<int:pk>', BorrarImagen.as_view(), name="borrarimagen"),
    path('buscar', SearchResultsListView.as_view(),
        name="buscaimagenes" ),
    #para autenticación
    path('imagenes',views.imagenes,name="login"),    
   
]

 
