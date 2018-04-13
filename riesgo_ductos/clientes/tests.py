from django.test import TestCase
from .models import Equipo, Empresa, Proyecto, PnID, Parametro

def crear_equipo(nombre):
    """
    Crea un equipo dado un nombre
    """
    empresa = Empresa.objects.create(código=5, nombre="Empresa 1")
    proyecto = Proyecto.objects.create(nombre="Proyecto 1", empresa=empresa)
    pnid = PnID.objects.create(nombre="PnID 1", proyecto=proyecto)
    equipo = Equipo.objects.create(nombre="E1", cliente=empresa, pnid=pnid)
    return equipo

class EquipoTest(TestCase):
    def test_crea_equipo(self):
        crear_equipo(nombre="E1")
        self.assertQuerysetEqual(
            Equipo.objects.all(),
            ['<Equipo: E1>']
        )

class ParametroTest(TestCase):
    def test_crea_parametro(self):
        parametro = Parametro(nombre="Parametro 1")
        self.assertQuerysetEqual(
            Parametro.objects.all(),
            []
        )
        parametro.save()
        self.assertQuerysetEqual(
            Parametro.objects.all(),
            ['<Parametro: Parametro 1>']
        )
