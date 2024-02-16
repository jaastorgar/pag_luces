from django.contrib import admin
from .models import Cliente, Producto, Reserva, Region, Comuna

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Reserva)
admin.site.register(Region)
admin.site.register(Comuna)