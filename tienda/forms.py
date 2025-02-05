from django.forms import ModelForm
from productos.models import Producto

class CargarForm(ModelForm):
    class Meta:
        model=Producto
        fields = ['producto', 'fecha_publicacion', 'imagen']

    def _init_(self, *args, **kwargs):
        super(CargarForm, self)._init_(*args, **kwargs)