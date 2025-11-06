from django.urls import path
from .import views
app_name= "tienda" # Clave para usar 'tienda:por_categoria' en los templates

urlpatterns =[
    path('', views.tienda, name='enlace'),
    #path('categoria/<int:categoria_id>/', views.tienda, name='por_categoria'),
    path('<slug:categoria_slug>/', views.tienda, name='por_categoria'),
]