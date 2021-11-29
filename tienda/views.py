from django.views import generic
from django.db.models import query_utils
from django.shortcuts import render
from .models import Producto
from django.db.models import Q


# Create your views here.

def tienda (request):
    productos=Producto.objects.all()
    return render (request, "tienda/tienda.html",{"productos":productos})



class ProductoListView(generic.ListView):
    '''Vista genérica para nuestro listado de productos'''
    model = Producto
    paginate_by = 15
    queryset = Producto.objects.all().order_by('nombre')


class SearchResultsListView():
    model = Producto
    context_object_name ='producto_list'
 
    def get_queryset(self): 
       
        query = self.request.GET.get('q')
        q1 = Q(nombre_producto_icontains = query)
        return Producto.objects.filter(q1)