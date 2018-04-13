from django.db import models
from django.utils import timezone

class TipoTel(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Telefono(models.Model):
    telefono = models.IntegerField(primary_key=True)
    tipo = models.ForeignKey(TipoTel, on_delete=models.PROTECT)
    def __str__(self):
        return str(self.telefono)+" - "+self.tipo.nombre


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

class Parametro(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    # class Meta:
    #     abstract = True

class Equipo(models.Model):
    cliente = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=255)
    descripción = models.TextField()
    pnid = models.ForeignKey(PnID, on_delete=models.PROTECT)
    parametros = models.ManyToManyField(Parametro, through='HEquipoParametro')

    def __str__(self):
        return self.nombre

class Historia(models.Model):
    fecha = models.DateTimeField(default=timezone.now)

class HInspeccion(Historia):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)

class HMantenimiento(Historia):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)

class HEquipo(Historia):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)

class Formula(models.Model):
    nombre = models.CharField(max_length=255)
    formula = models.TextField()

    def calc(self, equipo):
        return eval(self.formula)

class HEquipoParametro(Historia):
    equipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    parametro = models.ForeignKey(Parametro, on_delete=models.PROTECT)
    valor = models.FloatField()

    def __str__(self):
        return str(self.fecha) + " " + str(self.equipo) + " " + str(self.parametro) + " " + str(self.valor)

    @staticmethod
    def get_ultimo_valor(equipo, parametro):
        valor = HEquipoParametro.objects.filter(equipo=equipo, parametro=parametro).order_by('-fecha')
        if valor:
            return valor[0].valor
        return None

class Enum(Parametro):
    valor = models.IntegerField()

class Fecha(Parametro):
    valor = models.DateField()

class Numero(Parametro):
    valor = models.FloatField()

class Mapa(models.Model):
    enum = models.ForeignKey(Enum, on_delete=models.PROTECT)
    clave = models.CharField(max_length=255)
    valor = models.IntegerField()

    def __str__(self):
        return self.clave