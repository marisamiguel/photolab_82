from django.contrib import admin

# Register your models here.

from imagenes.models import Imagen
# Register your models here.

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    pass