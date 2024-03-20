# Generated by Django 5.0.3 on 2024-03-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(default='default', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]