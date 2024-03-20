from django.urls import path
from .views import registro, inicio_sesion, recuperar_contrasena


urlpatterns = [
    path('registro/', registro, name='registro'),
    path('inicio-sesion/', inicio_sesion, name='inicio_sesion'),
    path('recuperar-contrasena/', recuperar_contrasena, name='recuperar_contrasena'),
]