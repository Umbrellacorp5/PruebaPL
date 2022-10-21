from django.shortcuts import render
from django.http import HttpResponse
from app.forms import CrearProfesor
# Create your views here.

def index(request):
    #form = CrearProfesor()
    form = CrearProfesor(request.POST)
    if request.method == "POST":
        if form.is_valid():
        #print(request.POST)
            form.save()
    return render(request, 'index.html', {'form': form})


