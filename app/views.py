from dataclasses import field
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Nombre
from app.forms import CrearProfesor
# Create your views here.

def index(request):
    #form = CrearProfesor()
    form = CrearProfesor(request.POST)
    if request.method == "POST":
        nom = Nombre.objects.all()
        for n in nom:
            print('{0} - {1}'.format(n.fname, n.lname))
        form.fname = request.POST.get('fname')
        form.lname = request.POST.get('lname')
        if form.fname == n.fname:
            print("buenazo")

        #print(request.POST)
          
    return render(request, 'index.html', {'form': form})


