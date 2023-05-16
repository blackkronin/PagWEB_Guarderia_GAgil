from django.db import models

# Create your models here.

class Reserva(models.Model):
    cod = models.CharField(primary_key=True,max_length=6)
    nombrehijo = models.CharField(max_length=25)
    ruthijo = models.CharField(max_length=12)
    fecha = models.DateField()
    horas_reserva = models.PositiveSmallIntegerField()