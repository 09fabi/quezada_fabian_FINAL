from django.db import models
from django.utils import timezone

class Inscrito(models.Model):
    ESTADOS = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    )

    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    fecha_inscripcion = models.DateTimeField(default=timezone.now)
    institucion = models.ForeignKey('Institucion', on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='RESERVADO')
    observacion = models.TextField(blank=True)

class Institucion(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

"""--------------------------------------"""
"""   Desarrollado por: Fabian Quezada   """
"""--------------------------------------"""