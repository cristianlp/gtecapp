from django.db import models

class Organismo(models.Model):
    NACIONAL = 'NAC'
    PROVINCIAL = 'PROV'
    MUNICIPAL = 'MUN'
    INTERNACIONAL = 'INT'
    nombre = models.CharField(max_length=500)
    NIVEL_ORGANISMO_CHOICES = (
        (NACIONAL, 'Nacional'),
        (PROVINCIAL, 'Provincial'),
        (MUNICIPAL, 'Municipal'),
        (INTERNACIONAL, 'Internacional'),
    )
    nivel = models.CharField(max_length=3,
                                      choices=NIVEL_ORGANISMO_CHOICES,
                                      default=NACIONAL)
    def __str__(self):
        return self.nombre


class Instrumento(models.Model):
    nombre = models.CharField(max_length=500)
    organismo = models.ForeignKey(Organismo)
    descripcion = models.TextField(max_length=2000, blank=True)
    web = models.URLField(blank=True)

    def __str__(self):
        return self.nombre


class Convocatoria(models.Model):
    nombre = models.CharField(max_length=100)
    instrumento = models.ForeignKey(Instrumento)
    desde = models.DateField(blank=True)
    hasta = models.DateField(blank=True)
    monto_maximo = models.IntegerField(blank=True)
    es_anr = models.BooleanField(verbose_name='Es ANR?', default=False)
    web = models.URLField(blank=True)
    observaciones = models.TextField(max_length=2000, blank=True)

    def __str__(self):
       return self.nombre
