# Generated by Django 4.2.1 on 2024-02-22 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCliente', models.CharField(max_length=50, verbose_name='Nombre del cliente')),
                ('telefono', models.IntegerField(blank=True, null=True, verbose_name='Telefono del cliente')),
                ('direccion', models.CharField(blank=True, max_length=60, null=True, verbose_name='Direccion del cliente')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
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
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechainicio', models.DateField()),
                ('fechafin', models.DateField()),
                ('cantidad', models.PositiveBigIntegerField(default=1)),
                ('comentario', models.TextField()),
                ('terminocondicion', models.BooleanField(default=False, verbose_name='Acepto los terminos y condiciones')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='comuna',
            field=models.ManyToManyField(blank=True, to='core.comuna'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='region',
            field=models.ManyToManyField(blank=True, to='core.region'),
        ),
    ]
