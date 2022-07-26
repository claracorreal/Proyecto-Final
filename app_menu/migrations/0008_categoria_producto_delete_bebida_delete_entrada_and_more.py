# Generated by Django 4.0.4 on 2022-08-08 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_menu', '0007_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=400)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='bebidas')),
                ('modificacion', models.DateField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_menu.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Bebida',
        ),
        migrations.DeleteModel(
            name='Entrada',
        ),
        migrations.DeleteModel(
            name='Plato',
        ),
        migrations.DeleteModel(
            name='Postre',
        ),
    ]
