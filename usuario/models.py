from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import time

class Datosusuario(models.Model):
    usuario = models.OneToOneField(User, blank=False, null=True, on_delete=models.CASCADE, related_name="perfil")
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", default='defecto/defecto.png', blank=True, null=True)
    nombre               =models.CharField(max_length=50)
    apellido             =models.CharField(max_length=50)
    fecha_nacimiento     =models.CharField(max_length=30, blank=True)
    pais                 =models.CharField(max_length=30, blank=True)
    provincia            =models.CharField(max_length=40, blank=True)
    ciudad               =models.CharField(max_length=40, blank=True)
    domicilio            =models.CharField(max_length=80, blank=True)
    codigo_postal        =models.CharField(max_length=50, blank=True)
    telefono             =models.CharField(max_length=30, blank=True)
    celular              =models.CharField(max_length=30, blank=True)
    documento            =models.CharField(max_length=30, blank=True)
    cuit                 =models.CharField(max_length=30, blank=True)
    #email = models.EmailField(max_length=128, blank=True, null=True, default='---@gmail.com')
    
    def __str__(self):
        return self.usuario.username


