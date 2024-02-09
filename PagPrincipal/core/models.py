from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=50, verbose_name='Nombre del cliente')
    telefono = models.CharField(max_length=15, blank=True, null=True,
    verbose_name='Telefono del cliente')
    direccion = models.CharField(max_length=60, blank=True, null=True,
    verbose_name='Direccion del cliente')
    correo = models.EmailField(default = 'correo@example.com')

    def __str__ (self):
        return self.nombreCliente 


class Producto(models.Model):
    nombre = models.CharField(max_length=100,
    verbose_name='Nombre del producto')
    descripcion = models.TextField(verbose_name='Descripcion del producto')
    precio = models.IntegerField(verbose_name='Precio del producto')
    stock = models.IntegerField(verbose_name='Stock del producto')
    imagen = models.ImageField(upload_to='', null=True, 
    blank=True, verbose_name='Imagen del producto')
    
    def __str__ (self):
        return self.nombre
    
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    comentario = models.TextField()
    terminocondicion = models.BooleanField(default = False,
    verbose_name = 'Acepto los terminos y condiciones')

    def __str__ (self):
        return f'Reserva para {self.producto.nombre} de {self.producto.stock} tambien {self.cliente.nombreCliente} de {self.cliente.correo} de {self.cliente.telefono} de {self.cliente.direccion}'

class InicioSesion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    contrasena = models.CharField(max_length = 20, verbose_name = 'Contraseña')

    def __str__ (self):
        return self.cliente.correo