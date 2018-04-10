from django.db import models

class Telefono(models.Model):
    telefono = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.telefono


class Empresa(models.Model):
    código = models.CharField(primary_key=True, max_length=255)
    nombre = models.CharField(max_length=255)
    telefonos = models.ManyToManyField(Telefono)
    def __str__(self):
        return self.nombre


class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    telefonos = models.ManyToManyField(Telefono)
    def __str__(self):
        return self.nombre + " " + self.empresa.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre + " " + self.empresa.nombre

class PnID(models.Model):
    nombre = models.CharField(max_length=255)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre + " " + self.proyecto.nombre

class Equipo(models.Model):
    cliente = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=255)
    descripción = models.TextField()
    pnid = models.ForeignKey(PnID, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Historia(models.Model):
    fecha = models.DateTimeField()

class HInspeccion(Historia):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)

class HMantenimiento(Historia):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)

class HEquipo(Historia):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)

class Formula(models.Model):
    nombre = models.CharField(max_length=200)

class Parametro(models.Model):
    formula = models.ForeignKey(Formula, on_delete=models.PROTECT)

class HEquipoParametro(Historia):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    parametro = models.ForeignKey(Parametro, on_delete=models.PROTECT)

