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
    #crear,modificar,csv,json imagenes
    path('crear', views.ImagenCreateView.as_view(),
        name="creaimagen" ),
    #path ('borrar/<int:pk>/', views.BorrarImagen().as_view(), name="eliminar"),
    path('modificar/<int:pk>/', views.ModificarImagen.as_view(), name="modificarimagen"),
    path ('imagen_csv',views.imagenes_csv, name="imagenes_csv"),
    path ('imagen_json',views.imagenes_json, name="imagenes_json"),
    path('buscar', SearchResultsListView.as_view(),
        name="buscaimagenes" ),
    #para autenticación
    path('imagenes',views.imagenes,name="login"),    
   
]

 
