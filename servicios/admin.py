from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Servicio
#modifico mi Admin 
admin.site.site_header="Bienvenidos al portal del Administrador"
admin.site.site_title="Portal Servicios"
admin.site.index_title="Bienvenidos al portal del Administrador"

# Register your models here.Modifico la apariencia del Admin 
# Creo un list_display y un buscador por titulo

class ServicioAdmin(admin.ModelAdmin):
    list_display = ['titulo','contenido','imagen']
    search_fields=['titulo']
    list_filter=['titulo','contenido','imagen']
    
    pass

admin.site.register(Servicio, ServicioAdmin)