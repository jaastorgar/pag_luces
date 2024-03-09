from django.urls import path
from .views import home, arriendo, generar_informe_completo, buscar_productos, detalle_producto


urlpatterns = [
    path('', home, name="home"),
    path('arriendo/', arriendo, name="arriendo"),
    path('informe_completo/', generar_informe_completo, name='informe_completo'),
    path('buscar/', buscar_productos, name = 'buscar_productos'),
    path('detalle_producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
]