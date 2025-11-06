from django.shortcuts import render, get_object_or_404
from .models import Servicio
from categorias.models import Categoria


def tienda(request, categoria_slug=None):
    
    if categoria_slug:
        # obtener la categoria actual por el slug
        categoria= get_object_or_404(Categoria, slug=categoria_slug)
        # filtrar los servicios de esa categoria
        servicios_tienda= Servicio.objects.all().filter(
            categoria=categoria,
            esta_disponible=True
        )
        
    else:
        # Si no hay slug, mostrar todos los servicios disponibles
        categoria=None
        servicios_tienda= Servicio.objects.all().filter(esta_disponible=True)
    
    contar_servicios= servicios_tienda.count()

    # Contexto que se pasa al template
    context = {
        "categoria_actual": categoria,
        "servicios_tienda":servicios_tienda,
        "contar_servicios":contar_servicios,
    }

    return render(request, 'tienda/tienda_repo.html',context)
