from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

def home(request):
    tareas=Tarea.objects.all()
    context={'tareas':tareas}
    return render(request, 'todo/home.html', context)

def add(request):
    if request.method=="POST":
        form=TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TareaForm()
    
    context={'form':form}
    return render(request, 'todo/add.html', context)