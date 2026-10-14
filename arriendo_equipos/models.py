from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio en CLP")
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Arriendo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.CharField(max_length=100)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio en CLP")

    def __str__(self):
        return f"{self.cliente} - {self.equipo.nombre} - {self.precio_arriendo} CLP"