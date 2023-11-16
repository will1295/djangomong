from django.shortcuts import render
from .models import Estudiante

# Create your views here.

def list_est(request):
    estudiantes = Estudiante.objects.all()
    return render(request,"lista.html",{"estudiante":estudiantes})