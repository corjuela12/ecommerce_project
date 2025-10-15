from django.contrib import admin

# Register your models here.

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = (
    "nombre",
    "categoria",
    "costo",
    "stock",
    "esta_disponible",
    "fecha_creacion",
    "fecha_modificacion",
    )
    list_filter = ("categoria", "esta_disponible")#filtros a la derecha.
    search_fields = ("nombre", "descripcion")#agrega barra de búsqueda.
    list_editable = ("costo", "stock", "esta_disponible")#permite editar algunos campos desde la lista sin entrar al objeto.
    prepopulated_fields = {"slug": ("nombre",)}#hace que el slug se llene automáticamente con el nombre.

admin.site.register(Producto, ProductoAdmin)  # Registro manual (sin decorador)
