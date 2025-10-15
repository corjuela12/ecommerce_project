from django.contrib import admin
from .models import Categoria
# Register your models here.
#admin.site.register(Categoria)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=("nombre_categoria", "slug","descripcion")
    prepopulated_fields= {
        'slug': ('nombre_categoria',)
    }

    search_fields=("nombre_categoria","descripcion")

    list_filter=("nombre_categoria",)

    list_per_page= 2