from django import forms
from django.shortcuts import redirect, render
from .models import Tarea

class TareaForm(forms.ModelForm):
    tareas=Tarea.objects.all()
    class Meta:
        model=Tarea
        fields=['tarea']


