from django.conf import settings
from django.conf.urls import include, static

from django.urls import path
from imagenes.views import *
from . import views



urlpatterns = [
    path('',views.imagenes,name="home"),
    path('imagenes',views.imagenes,name="imagenes"),
    path('listar', views.ImagenesListView.as_view(), 
        name='Listado de Imagenes'),
    path('crear', views.ImagenCreateView.as_view(),
        name="creaimagen" ),
    #path('borrar', views.BorrarImg.as_view(), name='borrarimagen'),
    path('buscar', SearchResultsListView.as_view(),
        name="buscaimagenes" ),
    path('imagenes',views.imagenes,name="login"),    
   
]
 
