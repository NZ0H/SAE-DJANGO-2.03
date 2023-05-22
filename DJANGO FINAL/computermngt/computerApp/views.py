from django.shortcuts import render,get_object_or_404,redirect
from .models import Machine,Personnel
from .forms import AddMachineForm, DeleteMachineForm,AddPersonnelForm,DeletePersonnelForm
import requests
import json

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
    type_materiel = request.GET.get('type')
    if type_materiel:
        machines = machines.filter(type_materiel=type_materiel)
    context = {
        'machines' : machines,
        'type_materiel' : type_materiel,
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
    context = {'machine':machine}
    return render(request,'computerApp/machine_detail.html',context)

def machine_add_form(request):
    if request.method == 'POST' : 
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(
                nom = form.cleaned_data['nom'],
                lieu_infrastructure = form.cleaned_data['lieu_infrastructure'],
                maintenanceDate = form.cleaned_data['maintenanceDate'],
                type_materiel = form.cleaned_data['type_materiel']
                )
            new_machine.save()
            return redirect('machines')
    else :
        form = AddMachineForm()
    context ={'form':form}
    return render(request,'computerApp/machine_add.html',context)

def machine_delete_form(request):
    if request.method == 'POST':
        form = DeleteMachineForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            phrase_confirmation = form.cleaned_data['phrase_confirmation']
            machine = Personnel.objects.filter(id=id).first()
            if machine and phrase_confirmation == "Je confirme la suppression de l'utilisateur":
                machine.delete()
                return redirect('personnels')
            else:
                error_msg = "ID inexistant ou phrase de confirmation invalide."
                context = {'form': form, 'error_msg': error_msg}
                return render(request, 'computerApp/machine_del.html', context)
    else:
        form = DeleteMachineForm()
    context = {'form': form}
    return render(request, 'computerApp/machine_del.html', context)

def personnel_detail_view(request,pk):
    personnel = get_object_or_404(Personnel,id=pk)
    context = {"personnel":personnel}
    return render(request,'computerApp/personnel_detail.html',context)

def personnel_add_form(request):
    if request.method == 'POST':
        form = AddPersonnelForm(request.POST or None)
        if form.is_valid():
            new_personnel = Personnel(
                nom=form.cleaned_data['nom'],
                prenom=form.cleaned_data['prenom'],
                email=form.cleaned_data['email'],
                poste=form.cleaned_data['poste'],
                civilite = form.cleaned_data['civilite']
            )
            new_personnel.save()
            return redirect('personnels')
    else:
        form = AddPersonnelForm()

    context = {'form': form}
    return render(request, 'computerApp/personnel_add.html', context)

def personnel_delete_form(request):
    if request.method == 'POST':
        form = DeletePersonnelForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            phrase_confirmation = form.cleaned_data['phrase_confirmation']
            personnel = Personnel.objects.filter(id=id).first()
            if personnel and phrase_confirmation == "Je confirme la suppression de l'utilisateur":
                personnel.delete()
                return redirect('personnels')
            else:
                error_msg = "ID inexistant ou phrase de confirmation invalide."
                context = {'form': form, 'error_msg': error_msg}
                return render(request, 'computerApp/personnel_del.html', context)
    else:
        form = DeletePersonnelForm()
    context = {'form': form}
    return render(request, 'computerApp/personnel_del.html', context)



def infrastructure(request):
    machines = Machine.objects.all()
    infrastructure = request.GET.get('type')
    if infrastructure:
        machines = machines.filter(lieu_infrastructure=infrastructure)
    context = {
        'machines' : machines,
        'infrastrucutre':infrastructure,
    }
    return render(request,'computerApp/infrastructure.html',context)


def feature(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/24.48.0.1')
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    return render(request, 'computerApp/feature.html', {'data': location_data})
