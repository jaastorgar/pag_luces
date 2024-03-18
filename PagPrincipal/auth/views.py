from django.shortcuts import render

# Create your views here.
def registro(request):

    return render(request, 'auth/registro.html')

def inicio_sesion(request):

    return render(request, 'auth/inicio_sesion.html')

def recuperar_contrasena(request):

    return render(request, 'auth/recuperar_contrasena.html')