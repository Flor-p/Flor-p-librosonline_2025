from django.shortcuts import render
from django.contrib.auth import logout

def pagina_logout(request):
    params={}
    logout(request)
    return render(request, "usuario/logout.html", params)