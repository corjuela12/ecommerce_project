from django.urls import path
from .import views

app_name="home"

urlpatterns = [
    # Ruta principal → se muestra al entrar en http://127.0.0.1:8000/
    path("", views.home, name="home"),
    
    # Ejemplo alternativo: esta ruta mostraría la misma vista en http://127.0.0.1:8000/home/
    # path("home/", views.home, name="home"),
]