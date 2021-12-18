
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from imagenes.models import Imagen
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

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
class ModificarImagen(SuccessMessageMixin, generic.UpdateView):
    model = Imagen
    fields = '__all__'
    template_name = 'imagenes/modificar_imagen.html'
    success_url = '/'
    success_message = "%(titulo)s se ha modificado correctamente" 
    #Eliminacion de Registros


class BorrarImagen(SuccessMessageMixin,generic.DeleteView):
    model = Imagen
    fields = '__all__'
    success_url = '/' 
    success_message = "La Imagen se ha borrado correctamente"
    template_name = 'imagen_borrar.html'

    success_url = '/'
    # form_class = AuthorForm
    success_message = "%(titulo)s se ha borrado correctamente"

    def delete(self, request, *args, **kwargs):
    
        return super(BorrarImagen, self).delete(
            request, *args, **kwargs)

class BorrarImg(generic.DeleteView):
        model = Imagen
        
        template_name = 'imagenes/imagen_borrar.html'

        def get_success_url(self):
                return reverse_lazy('ImagenesListView', kwargs={'pk': self.object.imagenes.id})