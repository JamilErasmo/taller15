from django.db import models

# Create your models here.
from django.db import models

class Edificio(models.Model):
    RESIDENCIAL = 'residencial'
    COMERCIAL = 'comercial'
    TIPO_CHOICES = [
        (RESIDENCIAL, 'Residencial'),
        (COMERCIAL, 'Comercial'),
    ]
    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return self.nombre

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Departamento(models.Model):
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_de_cuartos = models.PositiveIntegerField()

    def __str__(self):
        return f"Departamento {self.id}"
