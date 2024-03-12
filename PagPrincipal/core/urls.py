from django.urls import path, include
from .views import home, arriendo, generar_informe_completo, buscar_productos, detalle_producto, cliente_login, registrar_cliente


urlpatterns = [
    path('', home, name="home"),
    path('arriendo/', arriendo, name="arriendo"),
    path('informe_completo/', generar_informe_completo, name='informe_completo'),
    path('buscar/', buscar_productos, name = 'buscar_productos'),
    path('detalle_producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('cliente_login/', cliente_login, name='cliente_login'),
    path('registrar_cliente/', registrar_cliente, name='registrar_cliente'),
]