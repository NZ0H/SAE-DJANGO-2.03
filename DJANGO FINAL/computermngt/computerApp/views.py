from django.shortcuts import render,get_object_or_404,redirect
from .models import Machine,Personnel
from .forms import AddMachineForm


def index(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()
    context = {
        'machines' : machines,
        'personnels' : personnels,
    }
    return render(request,'templates/index.html',context)

def liste_machines(request):
    machines = Machine.objects.all()
    context = {
        'machines' : machines,
    }
    return render(request,'templates/computerApp/liste_machines.html',context)

def liste_personnels(request):
    personnels = Personnel.objects.all()
    context = {
        'personnels' : personnels,
    }
    return render(request,'templates/computerApp/liste_personnels.html',context)

def machine_detail_view(request,pk):
    machine = get_object_or_404(Machine,id=pk)
    context = {"machine":machine}
    return render(request,'computerApp/machine_detail.html',context)

def machine_add_form(request):
    if request.method == 'POST' : 
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else :
        form = AddMachineForm()
            
    context ={'form':form}
    return render(request,'computerApp/machine_add.html',context)