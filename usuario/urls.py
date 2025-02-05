from django.urls import path
from vistaprevia import views
from usuario import views_login
from usuario import views_logout
#from usuario import views_registro

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views_login.pagina_login, name='login'),
    path('logout', views_logout.pagina_logout, name='logout'),
    #path('registro', views_registro.pagina_registro, name='registro'),
]