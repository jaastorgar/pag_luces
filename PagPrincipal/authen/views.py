from django.shortcuts import render, redirect
from core.forms import ClienteLoginForm, ClienteRegistroForm
from django.contrib.auth import authenticate, login
from allauth.account.forms import ResetPasswordForm

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio_sesion')
    else:
        form = ClienteRegistroForm()
    return render(request, 'authen/registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        form = ClienteLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigir a la página de inicio
    else:
        form = ClienteLoginForm()
    return render(request, 'authen/inicio_sesion.html', {'form': form})

def recuperar_contrasena(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'authen/recuperar_contrasena_confirmacion.html')
    else:
        form = ResetPasswordForm()
    return render(request, 'authen/recuperar_contrasena.html', {'form': form})