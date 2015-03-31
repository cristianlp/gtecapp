from django.db import models

from integrantes.models import Integrante

class Visita(models.Model):
    fecha_visita = models.DateField()
    visitada_por = models.ForeignKey(Integrante)
    motivo = models.TextField(blank=True)

    def __str__(self):
        return str(self.fecha_visita)


class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
       return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    responsable = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    ciudad = models.ForeignKey(Ciudad)

    def __str__(self):
       return self.nombre
