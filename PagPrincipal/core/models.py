from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=50, verbose_name='Nombre del cliente')
    telefono = models.CharField(max_length=15, blank=True, null=True,
    verbose_name='Telefono del cliente')
    direccion = models.CharField(max_length=60, blank=True, null=True,
    verbose_name='Direccion del cliente')

    def __str__(self):
        return self.nombreCliente 


class Producto(models.Model):
    nombre = models.CharField(max_length=100,
    verbose_name='Nombre del producto')
    descripcion = models.TextField(verbose_name='Descripcion del producto')
    precio = models.IntegerField(verbose_name='Precio del producto')
    stock = models.IntegerField(verbose_name='Stock del producto')
    imagen = models.ImageField(upload_to='', null=True, 
    blank=True, verbose_name='Imagen del producto')
    
    def __str__(self):
        return self.nombre