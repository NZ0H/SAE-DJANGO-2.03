from django.shortcuts import render
from .models import Machine,Personnel

def index(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()
    context = {
        'machines' : machines,
        'personnels' : personnels,
    }
    return render(request,'templates/index.html',context)

def liste_ordi(request):
    machines = Machine.objects.all()
    context = {
        'machines' : machines,
    }
    return render(request,'templates/computerApp/liste_computer.html',context)
    
