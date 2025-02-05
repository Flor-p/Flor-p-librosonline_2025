from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from captcha.fields import CaptchaField

class ConsultaForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Consulta
        fields = ['nombre', 'descripcion', 'mail', 'telefono', 'fecha']

    def send_email(self):
        nombre = self.cleaned_data['nombre']
        descripcion = self.cleaned_data['descripcion']
        mail = self.cleaned_data['mail']
        telefono = self.cleaned_data['telefono']
        fecha = self.cleaned_data['fecha']

        # Aquí implementa la lógica para enviar el correo electrónico
        print(f"Enviando correo: {nombre}, {descripcion}, {mail}, {telefono}, {fecha}")
        
        
        # A PARTIR DE ACÁ AGREGO LA LÓGICA DE ENVÍO DE MAIL
   
