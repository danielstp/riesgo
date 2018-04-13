# ADELGAZAMIENTO:
## Tipo de daño: Pérdida de espesor (CONSTANTE)
```sh
Equipo: 		V-103
[DATABASE.xls][dbDefSistema][Equipo]
```

```sh
Descripcion:	RECIPIENTE A PRESION
[DATABASE.xls][dbDefSistema][Descripcion]
```

```sh
Parte:			ENVOLVENTE
[DATABASE.xls][dbDefSistema][Parte]
```
```sh
Datos reportados a la fecha
[DATABASE.xls][dbTMSF_Thinning][Fecha]
```
```sh
Espesor al momento de entrar en el servicio actual
[DATABASE.xls][dbTMSF_Thinning][Espesor]
```
```sh
Tiempo en el servicio actual
[DATABASE.xls][dbTMSF_Thinning][Tiempo]
```
```sh
Año de entrada en servicio actual
[año](Datos reportados a la fecha) - (Tiempo en el servicio actual)
```
```sh
Corrsión Adm. al momento de entrar en el servicio actual
[DATABASE.xls][dbTMSF_Thinning][CA]
```
```sh
Mecanismo de daño (9 OPCIONES)[SELECT]
	1. Corrosión por Acido Clorhídrico (HCl)
	2. Corrosión por Acido Nafténico / Sulfídico a altas temperaturas
	3. Corrosión H2S/H2 a altas temperaturas
	4. Corrosión por Acido sulfúrico (H2SO4) 
	5. Corrosión por Acido fluorhidico (HF)
	6. Corrosión por agua ácida
	7. Corrosión por aminas
	8. Oxidación a altas temperaturas
	9. Otros...
```
```sh
Especificar (en el caso otros)
[INPUT - TEXT]
```
```sh
Velocidad de corrosion (mm/año)
[DATABASE.xls][dbTMSF_Thinning][Velocidad]
```
```sh
Fuente de datos de veloc. de corrosion (5 OPCIONES)[SELECT]
	Por antecedentes en equipos de servicio similar
	Calculada por Módulo Técnico API 581
	Calculada con valores medidos por UT
	Calculada con valores medidos en probetas de corrosion
	Otros...
```
```sh
Caracteristicas de la perdida de espesor (2 OPCIONES)[RADIO BUTTON]
	-LOCALIZADO
	-GENERALIZADO
```
```sh
Temperatura de la operación
[DATABASE.xls][dbTMSF_Thinning][Temp.Oper.]
```
```sh
Presión de la operación
[DATABASE.xls][dbTMSF_Thinning][Pres.Oper.]
```
```sh
MAWP (presión usada para determinar el minimo espesor de la pared admisible)
[DATABASE.xls][dbTMSF_Thinning][MAWP]
```
```sh
Categoria de efectividad de las inspecciones futuras (4 opciones, con campo de sugerencia)[SELECT]
	-MUY SATISFACTORIA
	-GENERALMENTE SATISFACTORIA
	-SATISFACTORIA
	-POCO SATISFACTORIA
```
```sh
* Sugerencia para Cat. efect. insp. fut.
=CONCATENAR("sugerida: Inspección de efectividad" ,AG42)
```
```sh
Número de inspecciones equivalentes realizadas
[DATABASE.xls][dbTMSF_Thinning][N° Inspec]
```
```sh
Frecuencia de proximas inspecciones
[DATABASE.xls][dbTMSF_Thinning][Frecuencia]
```
```sh
Sugerencia (^FrecProxInspec^)
=AG41
```
```sh
Año de la prox inspeccion
[DATABASE.xls][dbTMSF_Thinning][Prox. Inspec]
```
```sh
Tipo de monitoreo online (4 OPCIONES)[SELECT]
	-VARIABLES DE PROCESO + PROBETAS
	-VARIABLES DE PROCESO
	-PROBETAS
	-CUPONES
	-NINGUNO
```
```sh
Material de construccion [TMSF][APPENDIX G][AK52][Materiales]
	-SA 106 Gr B
	-SA 106 Gr C
	-SA 204M Gr B
	-SA 240 TP 304
	-SA 240 TP 304H
	-SA 240 TP 304L
	-SA 240 TP 316L
	-SA 240 TP 316LN
	-SA 266 Gr 2
	-SA 285 Gr A
	-SA 285 Gr B
	-SA 285 Gr C
	-SA 302 Gr B
	-SA 302 Gr D
	-SA 312 TP 304
	-SA 312 TP 304L
	-SA 312 TP 321H - Welded
	-SA 312 TP 321H - Seamless (< 3/16 in.)
	-SA 312 TP 321H - Seamless (>/= 3/16 in.)
	-SA 335 P11
	-SA 335 P22
	-SA 336 Gr F11 Cl 3
	-SA 387 Gr 11 Cl 2
	-SA 387 Gr 12 Cl 2
	-SA 508 Gr 3 Cl 1
	-SA 515 Gr 60
	-SA 515 Gr 65
	-SA 515 Gr 70
	-SA 516 Gr 55
	-SA 516 Gr 60
	-SA 516 Gr 65
	-SA 516 Gr 70
	-SA 533 Gr B Cl 2
	-SA 537 Cl 1 (<2 1/2" (65 mm))
	-SA 537 Cl 1 (2 1/2 - 4" (65 - 100 mm))
	-SA 541 Gr 22  Cl 3
```
```sh
Tensión de fluencia del material
[TMSF][APPENDIX G][AN55][Tension de Fluencia][Mpa]
```
```sh
Tensión de rotura del material
[TMSF][APPENDIX G][AP55][Tension de Rotura][Mpa]
```
```sh
Diámetro principal del equipo
[DATABASE.xls][dbTMSF_Thinning][Diametro]
```
```sh
Se trata de una cañería?(2 OPCIONES)[RADIO BUTTON]
	*SI			*NO
Si es cañería, preguntas extra:
	Presencia de puntos de inyeccion o mezcla(2 OPCIONES)[RADIO BUTTON]
	*SI			*NO
	Alta efectiv. de inspec. en puntos de inyec. o mezcla(2 OPCIONES)[RADIO BUTTON]
	*SI			*NO
	Presencia de Deadleg(2 OPCIONES)[RADIO BUTTON]
	*SI			*NO
	Alta efectividad de inspeccion para Deadleg(2 OPCIONES)[RADIO BUTTON]
	*SI			*NO
```
### Referencias
|Variable| Tabla|
| ------ | ------ |
|THINNING | dbTMSF_Thinning|
|SCC | dbTMSF_SCC |
|HTHA | dbTMSF_HTHA|
|F.Tube | dbTMSF_Furnace|
|M.Fatig | dbTMSF_Fatigue|
|B.Fract | dbTMSF_BF|
|Lining | dbTMSF_Lining|
|Ext.Dam | dbTMSF_ED|
