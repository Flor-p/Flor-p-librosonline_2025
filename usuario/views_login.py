from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def pagina_login(request):
    params = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("verimagenes")
        else:
            params["error"] = "Usuario o contraseña incorrectos"  # Mensaje de error opcional

    # Manejar GET o POST fallido
    return render(request, "usuario/login.html", params)
        
    
    




