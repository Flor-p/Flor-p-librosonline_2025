from django.urls import path
from contacto import views  # Importa las vistas desde el archivo views.py
from contacto.views import Contacto
from contacto.views import MensajeEnviado

urlpatterns = [
    path('', views.Contacto.as_view(), name='contacto'),  # Ruta para la vista Contacto
    path('mensaje_enviado', MensajeEnviado.as_view(), name="mensaje_enviado"), 
]