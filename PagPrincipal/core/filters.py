import django_filters
from .models import Reserva

class ReservaFilter(django_filters.FilterSet):
    cliente__nombreCliente = django_filters.CharFilter(
        field_name='carrito__cliente__nombreCliente',
        lookup_expr='icontains',
        label='Nombre del Cliente'
    )

    producto__nombre = django_filters.CharFilter(
        field_name='producto__nombre',
        lookup_expr='icontains',
        label='Nombre del Producto'
    )

    class Meta:
        model = Reserva
        fields = ['cliente__nombreCliente', 'producto__nombre', 'cantidad']