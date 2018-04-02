from django.db import models

class Telefono(models.Model):
    telefono = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.telefono


class Empresa(models.Model):
    código = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(max_length=255)
    telefonos = models.ManyToMany(Telefono)
    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    telefonos = models.ManyToMany(Telefono)
    def __str__(self):
        return self.nombre + " " + self.empresa.nombre


class Equipo(models.Model):
    cliente = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=255)
    descripción = models.TextField()

    def __str__(self):
        return self.nombre

