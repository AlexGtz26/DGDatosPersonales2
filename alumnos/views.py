# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import DatosPersonales

def index(request):
    return render(request, "alumnos/index.html")

def res(request):
    datos = DatosPersonales.objects.all()
    return render(request, "alumnos/resultado.html",{"alumnos":datos})


# Create your views here.
