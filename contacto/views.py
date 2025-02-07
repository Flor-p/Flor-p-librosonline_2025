from django.shortcuts import render
from django.views.generic import View, FormView
from django.urls import reverse_lazy  # Agregado
from contacto.forms import ConsultaForm

class Contacto(FormView):
    template_name = 'contacto/contacto.html'
    form_class = ConsultaForm
    success_url = reverse_lazy('contacto_exito')  # Cambiado a reverse_lazy

    def form_valid(self, form):
        form.save()
        form.send_email()  # Esto llama al método send_email() del formulario
        return super().form_valid(form)
    
class MensajeEnviado(View):
    template = 'contacto/mensaje_enviado.html'
    
    def get(self, request):
        return render(request, self.template, {'mensaje': "Aquí va un mensaje"})
