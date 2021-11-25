from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#crearemos una clase para cada Categoría

class Categoria(models.Model):
        nombre=models.CharField(max_length=50)
        
    
        class Meta:
            verbose_name='categoria'
            verbose_name_plural='categorias'

        def __str__(self):
         return self.nombre
  
  #FK Autor y relacion de muchos/muchos Categoria
class Post(models.Model):
        titulo=models.CharField(max_length=50)
        contenido=models.CharField(max_length=50)
        imagen=models.ImageField(upload_to='blog', null=True, blank=True)
        autor=models.ForeignKey(User, on_delete=models.CASCADE)
        categorias=models.ManyToManyField(Categoria)

        class Meta:
            verbose_name='post'
            verbose_name_plural='posts'

        def __str__(self):
         return self.titulo
