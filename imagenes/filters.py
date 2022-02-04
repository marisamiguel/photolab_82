from django.db.models import fields
import django_filters
from .models import *


class ImagenFilter(django_filters.FilterSet):
    class Meta:
        model = Imagen
        fields = '__all__'

