from django.urls import path
from tienda import views
from tienda.views import VerImagenes
from tienda.views import EjemploLocalStorage

urlpatterns = [
    path('cargar/', views.cargar_imagen, name="cargar"),
    path('<int:producto_id>/ver/', views.ver_imagen, name="ver"),  
    path('verimagenes/', VerImagenes.as_view(), name="verimagenes"),
    path('ejemplo_localstorage/', EjemploLocalStorage.as_view(), name="ejemplo_localstorage"),
]

