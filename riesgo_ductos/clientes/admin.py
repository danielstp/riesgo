from django.contrib import admin

from .models import (Telefono, Empresa, Contacto, Proyecto, PnID, Equipo,
    Historia, HInspeccion, HMantenimiento, HEquipo, Formula, Parametro, 
    HEquipoParametro)
admin.site.register(Telefono)
admin.site.register(Empresa)
admin.site.register(Contacto)
admin.site.register(Proyecto)
admin.site.register(PnID)
admin.site.register(Equipo)
admin.site.register(Historia)
admin.site.register(HInspeccion)
admin.site.register(HMantenimiento)
admin.site.register(HEquipo)
admin.site.register(Formula)
admin.site.register(Parametro)
admin.site.register(HEquipoParametro)