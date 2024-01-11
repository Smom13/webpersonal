from django.shortcuts import render
from .models import Project

def portfolio(request):
   projects = Project.objects.all()
   return render(request, "portfolio/portfolio.html",{'projects':projects}) #diccionario de contexto, se asigna nombre de variable para enviar los datos obtenidos