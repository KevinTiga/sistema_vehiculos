from django.contrib import admin
from .models import Cliente, Vehiculo, Alquiler, Reparacion, Empleado

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Vehiculo)
admin.site.register(Alquiler)
admin.site.register(Reparacion)
admin.site.register(Empleado)
