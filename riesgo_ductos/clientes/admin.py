from django.contrib import admin

from .models import Equipo, Empresa, Telefono, Contacto
admin.site.register(Equipo)
admin.site.register(Empresa)
admin.site.register(Telefono)
admin.site.register(Contacto)
