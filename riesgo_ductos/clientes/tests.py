from django.test import TestCase
from .models import Equipo, Empresa, Proyecto, PnID, Parametro, HEquipoParametro, Formula

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

class HEquipoParametroTest(TestCase):
    def test_crea_HEP(self):
        e1 = crear_equipo(nombre="E1")
        p1 = Parametro.objects.create(nombre="Parametro 1")
        HEquipoParametro.objects.create(equipo=e1, parametro=p1, valor=5.2)
        self.assertIsNot(
            HEquipoParametro.objects.all(),
            []
        )

    def test_get_ultimo_valor(self):
        e1 = crear_equipo(nombre="E1")
        p1 = Parametro.objects.create(nombre="Parametro 1")
        HEquipoParametro.objects.create(equipo=e1, parametro=p1, valor=5.2)
        import time
        time.sleep(1)
        HEquipoParametro.objects.create(equipo=e1, parametro=p1, valor=2.2)
        valor = HEquipoParametro.get_ultimo_valor(equipo=e1, parametro=p1)
        self.assertEqual(valor, 2.2)

class FormulaTest(TestCase):
    def test_calc(self):
        e1 = crear_equipo(nombre="E1")
        p1 = Parametro.objects.create(nombre="Parametro 1")
        HEquipoParametro.objects.create(equipo=e1, parametro=p1, valor=3)
        p2 = Parametro.objects.create(nombre="Parametro 2")
        HEquipoParametro.objects.create(equipo=e1, parametro=p2, valor=2)
        formula = Formula(nombre="Mi Formula", formula="HEquipoParametro.objects.get(equipo=Equipo.objects.get(nombre='E1'), parametro=Parametro.objects.get(nombre='Parametro 1')).valor*HEquipoParametro.objects.get(equipo=Equipo.objects.get(nombre='E1'), parametro=Parametro.objects.get(nombre='Parametro 2')).valor")
        resultado = formula.calc(equipo=e1)
        self.assertEqual(resultado, 6)