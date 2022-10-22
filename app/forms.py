import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from app.models import Nombre
 
class CrearProfesor(ModelForm):
    fname= forms.CharField(label="Nombre", max_length=255, min_length=3, required=True)
    lname= forms.CharField(label="Apellido", max_length=255, min_length=3, required=True)
   
    class Meta:
        model = Nombre
        fields = '__all__'

