from django.urls import path
from tienda import views
from tienda import views_agregar
from tienda.views import VerImagenes
from tienda.views import EjemploLocalSotage

urlpatterns = [
    path('cargar/', views.cargar_imagen, name="cargar"),
    path('<int:producto_id>/ver/', views.ver_imagen, name="ver"),  
    path('verimagenes/', VerImagenes.as_view(), name="verimagenes"),
    path('ejemplo_localstorage/', EjemploLocalSotage.as_view(), name="ejemplo_localstorage"),
    path("agregar/", views_agregar.agregar, name="agregar"),
]