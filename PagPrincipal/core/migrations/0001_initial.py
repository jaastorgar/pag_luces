# Generated by Django 5.0.3 on 2024-03-10 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('descripcion', models.TextField(verbose_name='Descripcion del producto')),
                ('precio', models.IntegerField(verbose_name='Precio del producto')),
                ('stock', models.IntegerField(verbose_name='Stock del producto')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen del producto')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre del cliente')),
                ('telefono', models.IntegerField(blank=True, null=True, verbose_name='Telefono del cliente')),
                ('direccion', models.CharField(blank=True, max_length=60, null=True, verbose_name='Direccion del cliente')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('comuna', models.ManyToManyField(blank=True, to='core.comuna')),
                ('region', models.ManyToManyField(blank=True, to='core.region')),
            ],
        ),
    ]
