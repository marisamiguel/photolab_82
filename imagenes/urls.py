from django.conf import settings
from django.conf.urls import static
from django.urls import path
from imagenes.views import *
from . import views



urlpatterns = [

    
    path('', views.ImagenesListView.as_view(), 
        name='Listado de Imagenes'),
    path('crear', views.ImagenCreateView.as_view(),
        name="creaimagen" ),
    
]
 
