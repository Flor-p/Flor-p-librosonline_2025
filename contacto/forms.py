from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from captcha.fields import CaptchaField

class ConsultaForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Consulta
        fields = ['nombre', 'descripcion', 'mail', 'telefono', 'fecha']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu Nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tu Mensaje', 'rows': 4}),
            'mail': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu Correo Electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu Teléfono'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def send_email(self):
        nombre = self.cleaned_data['nombre']
        descripcion = self.cleaned_data['descripcion']
        mail = self.cleaned_data['mail']
        telefono = self.cleaned_data['telefono']
        fecha = self.cleaned_data['fecha']

        # Aquí implementa la lógica para enviar el correo electrónico
        print(f"Enviando correo: {nombre}, {descripcion}, {mail}, {telefono}, {fecha}")
