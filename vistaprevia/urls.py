from django.urls import path
from vistaprevia import views
from vistaprevia.views import Templatetags1
from vistaprevia.views import para_ajax
from vistaprevia.views import BuscarLibro



urlpatterns = [
    path("", views.index, name="index"),
    path("templatetags1", Templatetags1.as_view(), name="templatetags1"),
    path("usar_ajax", views.para_ajax, name="usar_ajax"),
    path("buscar_libro/", BuscarLibro.as_view(), name="buscar_libro"),
]
