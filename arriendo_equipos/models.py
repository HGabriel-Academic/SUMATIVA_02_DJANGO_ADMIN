from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_arriendo = models.BigIntegerField(help_text="Precio en CLP")
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Arriendo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.CharField(max_length=100)
    precio_arriendo = models.BigIntegerField(help_text="Precio en CLP")

    def __str__(self):
        precio = self.precio_arriendo if self.precio_arriendo is not None else 0
        precio_formateado = "${:,.0f}".format(precio).replace(",", ".")
        nombre_equipo = self.equipo.nombre if self.equipo else "Equipo sin asignar"
        return f"{self.cliente} - {nombre_equipo} - ${precio_formateado}"
        