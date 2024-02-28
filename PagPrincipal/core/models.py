from django.db import models

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre 

class Cliente(models.Model):
    nombreCliente = models.CharField(max_length=50, verbose_name='Nombre del cliente')
    telefono = models.IntegerField(blank=True, null=True,
    verbose_name='Telefono del cliente')
    direccion = models.CharField(max_length=60, blank=True, null=True,
    verbose_name='Direccion del cliente')
    email = models.EmailField(blank=True, null=True)
    region = models.ManyToManyField('Region', blank = True) 
    comuna = models.ManyToManyField('Comuna', blank = True)

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
    
class Carrito(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Carrito de {self.cliente.nombreCliente}'
    
class Reserva(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad = models.PositiveBigIntegerField(default = 1)

    def __str__ (self):
        return f'Reserva para Cliente: {self.carrito.cliente.nombreCliente} del Producto: {self.producto.nombre}'