# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class DatosPersonales(models.Model):
    num_count = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    fechanacimiento = models.DateField()
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    domicilio = models.TextField()

# Create your models here.
