from django.contrib import admin

from .models import (Telefono, TipoTel, Empresa, Contacto, Proyecto, PnID,
    Equipo, Historia, HInspeccion, HMantenimiento, HEquipo, Formula, Parametro,
    HEquipoParametro, Formulario)

@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    fields = ('nombre', 'formula', 'calc')
    list_display = ['calc']
    # fieldsets = [(None, {'fields': ['nombre','calc']}),]
    readonly_fields = ['calc']
    def calc(self, obj):
        return obj.calc(Equipo.objects.get(pk=1))
    calc.allow_tags = True
    calc.short_description = 'Resultado'

class HEquipoParametroInline(admin.TabularInline):
    model = HEquipoParametro
    extra = 3


class EquipoAdmin(admin.ModelAdmin):
    inlines = [HEquipoParametroInline]
    search_fields = ['nombre']


admin.site.register(Telefono)
admin.site.register(TipoTel)
admin.site.register(Empresa)
admin.site.register(Contacto)
admin.site.register(Proyecto)
admin.site.register(PnID)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Historia)
admin.site.register(HInspeccion)
admin.site.register(HMantenimiento)
admin.site.register(HEquipo)
admin.site.register(Parametro)
admin.site.register(HEquipoParametro)
admin.site.register(Formulario)

admin.site.site_header = "Administración RBI"
admin.site.site_title = "Sitio de Administración del Sistema RBI"