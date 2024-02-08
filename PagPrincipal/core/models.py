from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCliente = models.CharField(max_length=50, verbose_name='Nombre del cliente')

    def __str__(self):
        return self.idCliente