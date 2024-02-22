from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, arriendo, iniciosesion, generar_informe_completo, reservas, busquedas
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('arriendo/', arriendo, name="arriendo"),
    path('inicioSesion/', iniciosesion, name="sesion"),
    path('informe_completo/', generar_informe_completo, name='informe_completo'),
    path('reservaLuces/', reservas, name = "reservas"),
    path('busquedas/', busquedas, name = "busquedas"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)