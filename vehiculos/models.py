from django.db import models
# Create your models here.

# Modelo Cliente
class Cliente(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    correo = models.EmailField(unique=True, blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.nombre


# Modelo Vehículo
class Vehiculo(models.Model):
    placa = models.CharField(max_length=6, unique=True, blank=False, null=False)
    marca = models.CharField(max_length=50, blank=False, null=False)
    modelo = models.CharField(max_length=50, blank=False, null=False)
    año = models.PositiveIntegerField(blank=False, null=False)
    estado = models.CharField(max_length=20,choices=[("Disponible", "Disponible"), ("Ocupado", "Ocupado")],default="Disponible",)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"


# Modelo Alquiler
class Alquiler(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.RESTRICT)
    fecha_alquiler = models.DateField(blank=False, null=False)
    fecha_devolucion = models.DateField(blank=False, null=False)

    def __str__(self):
        return f"Alquiler de {self.vehiculo} a {self.cliente}"


# Modelo Reparación
class Reparacion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField(blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return f"Reparación {self.fecha} - {self.vehiculo}"


# Modelo Empleado
class Empleado(models.Model):
    cedula = models.CharField(primary_key=True, max_length=10, unique=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    puesto = models.CharField(max_length=30, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nombre
