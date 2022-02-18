
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import ListView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from imagenes.models import Imagen
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import csv
import os
from django.http import HttpResponse
from django.http import JsonResponse


def imagenToDictionary(i):
    """
    A utility function to convert object of type IMG to a Python Dictionary
    """
    output = {}
    output["titulo"] = i.titulo
    output["file"] = i.file.path
    output["ancho"] = i.ancho
    output["fecha_subida"] = i.fecha_subida
    output["subida_por"] = str(i.subida_por)
    
    return output

# Function based view
def imagenes_json(request):
    # Single Blog
   

    # Multiple Blogs
    imagenes = models.Imagen.objects.all()
    tempImagenes = []

    # Converting `QuerySet` to a Python Dictionary
    
    for img in imagenes:
        tempImagenes.append(imagenToDictionary(img)) # Converting `QuerySet` to a Python Dictionary


    data = {
        
        "imagenes": tempImagenes
    }

    return JsonResponse(data)

def imagenes_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
    content_type='text/csv',
    headers={'Content-Disposition': 'attachment; filename="imagenes.csv"'},
    )

#configuramos el escritor y le pasamos una respuesta
    writer = csv.writer(response, dialect='excel')
#designar el Models   
    imagenes= Imagen.objects.all()

#añadir los encabezados a las columnas del csv s
    writer.writerow(['Titulo', 'Ancho', 'Alto',' Fecha_subida','Subida_por'])
#loop   
    for img in imagenes:
      writer.writerow([img.titulo, img.ancho,img.alto,img.fecha_subida,str(img.subida_por)])
    return response

# Create your views here.

def get_upload_to(instancia, filename):
    return instancia.get_upload_to(filename)

# vista para el buscador en background
class SearchResultsListView(ListView):
    model = Imagen
    context_object_name = 'imagenes'
    template_name = 'buscar.html'  # No usará la plantilla estándar del ListView
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            return Imagen.objects.filter(titulo__icontains=query)
        return []  # cuando entramos a buscar o si no se introduce nada

 # vista para la página de inicio de imagenes     
def imagenes(request):
    return render(request, "base.html")

 # vista para el list view de imagenes   
class ImagenesListView(ListView):
    model = Imagen
    template_name = 'imagenes/imagenes_list.html'
    context_object_name = 'imagenes'
    paginate_by = 10
    ordering = ['-fecha_subida']

 # vista para la página de crear  
class ImagenCreateView(SuccessMessageMixin, CreateView):
    model = Imagen
    fields = '__all__'
    template_name = 'imagenes/imagen_crear.html'

    success_url = '/'
    # form_class = AuthorForm
    success_message = "%(titulo)s se ha subido correctamente"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.subida_por = self.request.user
        return super().form_valid(form)


# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class ModificarImagen(SuccessMessageMixin,UpdateView):
    model = Imagen
    fields = ['titulo']
    template_name = 'imagenes/modificar_imagen.html'
    success_url = '/'
    success_message = "%(titulo)s se ha modificado correctamente" 
    
    # def modificar_imagen(request,imagen_id):
    #     return render (request,'imagenes/modificar_imagen.html')

class BorrarImagen(SuccessMessageMixin,DeleteView):
    model = Imagen
    fields=['titulo']
    template_name = 'imagenes/imagen_borrar.html'
    success_url = '/' 
    success_message = "%(titulo)s La Imagen se ha borrado correctamente"
    

