# ADELGAZAMIENTO API RP 581

Este factor de daño está asociado con componentes cuyos mecanismos de deterioro resultan en una pérdida localizada o generalizada de su espesor interno.

## Requerimientos
| Variable | Detalles | Tipo |
| ------ | ------ | ------ |
Nombre	|	Nombre del equipo	|	Texto
Parte	|	Ej: SEPARADOR GAS DE ENTRADA / FILTRO SEPARADOR DE ALTA |	Texto
Fecha	|	Datos reportados a la Fecha	|	dd/mm/yyyy
Espesor	|	Ultimo espesor medido	|	Milímetros
Tiempo	|	Años desde la ultima medicion de espesores | Años
CorrosionAdmisible	|	[CA] Corrosion admisible según diseño (normas API, ASME, etc)	|	Milímetros
OtroMecanismoDaño	|	Mecanismo de daño [otro]	|	Texto
MecanismoDaño	|	Mecanismo de daño	|	int(?) selección desde otra tabla
VelCorr	|	Velocidad de corrosion	| Milímetros/año
TemperOper	|	Temperatura de operacion	|	°C
PresionOper	|	Presion de operacion	|	kg/cm²
MAWP	|	Maximum allowable working pressure	|	kg/cm²
NumInspeccRealiz	|	Numero de inspecciones realizadas	|	int
FrecuenciaInpecc	|	Frecuencia de proximas inspecciones	|	años
AñoProxInspecc	|	Año de la proxima inspeccion	| yyyy
Material	|	Material de construccion	|	int(?) selección desde otra tabla
Diametro    |   ?   |   ?
ConfiabDatosCorr    |   Confiabilidad de los datos para la Velocidad de Corrosión  |    int(?) Alta/Media/Baja
TipoAdelg   |   TIpo de Adelgazamiento  |   int(?)  Localizado / Generalizado
EfectivInsp |   Categoría de efectividad de las inspecciones futuras    |   int(?) A/B/C/D/E
Monitoreo   |   Tipo de Monitoreo On-Line   |   int(?) Ninguno/var/var/probetas/cupones
EsCañeria   |   El equipo es cañería?   |   int(boolean?)  0/1
Inyeccion   |   Presencia de puntos de inyeccion o mezcla   | int(boolean?)  0/1  
EfecInyecc  |   Alta efectiv. de inspec. en puntos de inyec. o mezcla   |   int(boolean?)  0/1
Deadleg |   Presencia de Deadleg    |   int(boolean?)  0/1
EfecDeadleg |   Alta efectividad de inspeccion para Deadleg |   int(boolean?)  0/1
EspMin  |   Espesor minimo según normas |   Milímetros
VUR |   no se usa   |   ?
ND  |   Numero de inspecciones POCO EFECTIVAS realizadas    |   int
NC  |   Numero de inspecciones EFECTIVAS realizadas    |   int
NB  |   Numero de inspecciones GENERALMENTE EFECTIVAS realizadas    |   int
NA  |   Numero de inspecciones ALTAMENTE EFECTIVAS realizadas    |   int
E   |   Coeficiente de seguridad E  |   # Real


