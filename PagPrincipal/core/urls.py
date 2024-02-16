from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, arriendo, iniciosesion, generar_informe_completo

urlpatterns = [
    path('', home, name="home"),
    path('arriendo/', arriendo, name="arriendo"),
    path('inicioSesion/', iniciosesion, name="sesion"),
    path('informe_completo/', generar_informe_completo, name='informe_completo'),
]