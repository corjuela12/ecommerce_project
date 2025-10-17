from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    list_display = (
    "mostrar_imagen",
    "nombre",
    "categoria",
    "costo",
    "esta_disponible",
    "fecha_creacion",
    "fecha_modificacion",
    )
    list_filter = ("categoria", "esta_disponible")#filtros a la derecha.
    search_fields = ("nombre", "descripcion")#agrega barra de búsqueda.
    list_editable = ("costo", "esta_disponible")#permite editar algunos campos desde la lista sin entrar al objeto.
    prepopulated_fields = {"slug": ("nombre",)}#hace que el slug se llene automáticamente con el nombre.

    #  Función para mostrar miniatura de la imagen
    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="70" height="50" style="object-fit: cover; border-radius: 6px;"/>', obj.imagen.url)
        return "(Sin imagen)"
    mostrar_imagen.short_description = "Vista previa"  # título de la columna

admin.site.register(Servicio, ServicioAdmin)  # Registro manual (sin decorador)
