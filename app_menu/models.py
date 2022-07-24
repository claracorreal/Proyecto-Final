from django.db import models

class Entrada(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="entradas", null=True, blank=True)
    modificacion = models.DateField()

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="platos", null=True, blank=True)
    modificacion = models.DateField()

    def __str__(self):
        return f"{self.nombre: ${self.precio}}"

class Postre(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="postres", null=True, blank=True)
    modificacion = models.DateField()

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"

class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="bebidas", null=True, blank=True)
    modificacion = models.DateField()

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"



# Hice esta clase de Contacto, para poder tener un formulario tipo Form.
class Contacto (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} { self.apellido}"