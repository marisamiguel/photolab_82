from django.contrib import admin
from .models import Servicio

# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Servicio, ServicioAdmin)