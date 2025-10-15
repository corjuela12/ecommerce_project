from django.db import models

# Create your models here.

from categorias.models import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    descripcion = models.TextField("Descripción", max_length=300, blank=True)
    costo= models.IntegerField()
    imagen= models.ImageField(upload_to="imgs/productos/")# opcional despues se usa cloudinary
    stock = models.IntegerField()
    esta_disponible=models.BooleanField(default=True)
    categoria= models.ForeignKey(
        Categoria, on_delete = models.CASCADE # si se elimina una categoria tambien se elimina el producto

    )
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)#guarda automáticamente la fecha y hora cuando el objeto se crea por primera vez.
    fecha_modificacion = models.DateTimeField("Fecha de modificación", auto_now=True)#actualiza automáticamente la fecha y hora cada vez que se guarda (se modifica) el objeto.

    def __str__(self):
        return self.nombre