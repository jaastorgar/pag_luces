from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre 

class ClienteManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Crea y devuelve un usuario con el correo electrónico y la contraseña especificados.
        """
        if not email:
            raise ValueError('El correo electrónico es obligatorio')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Cliente(AbstractBaseUser):
    nombreCliente = models.CharField(max_length=50, verbose_name='Nombre del cliente')
    telefono = models.IntegerField(blank=True, null=True,
    verbose_name='Telefono del cliente')
    direccion = models.CharField(max_length=60, blank=True, null=True,
    verbose_name='Direccion del cliente')
    email = models.EmailField(blank=True, null=True)
    region = models.ManyToManyField('Region', blank = True) 
    comuna = models.ManyToManyField('Comuna', blank = True)

    objects = ClienteManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombreCliente', 'telefono', 'direccion', 'region', 'comuna']

    def __str__(self):
        return self.email

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