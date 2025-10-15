from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nombre_categoria= models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    descripcion=models.TextField(max_length=200, blank=True)
    
    def __str__(self):
        return self.nombre_categoria
    
    def get_url(self):
        return reverse("producto_por_categoria", args=[self.slug])