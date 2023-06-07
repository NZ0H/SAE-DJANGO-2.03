from django.shortcuts import render, get_object_or_404, redirect
from .models import Machine,Personnel
from .forms import AddMachineForm, DeleteMachineForm,AddPersonnelForm,DeletePersonnelForm,IPAddressForm
from django.contrib import messages
from django.utils import timezone


# gestion d'allumer,eteind, maintenance
import random
from datetime import date

# module de login django
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required

# bibliotheque pour la feature
import folium
import ipaddress
import bigdatacloudapi

#page racine
def index(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()
    context = {
        'machines' : machines,
        'personnels' : personnels,
    }
    return render(request,'index.html',context)

#vu liste machine
@login_required
def liste_machines(request):
    machines = Machine.objects.all()
    type_materiel = request.GET.get('type')
    date_m = (date.today()).strftime('%Y-%m-%d')
    for machine in machines:
        machine.etat = random.choice(['on', 'off'])
        print(machine.maintenanceDate,date_m)
        if machine.maintenanceDate.strftime('%Y-%m-%d') == date_m:
            print(machine.maintenanceDate)
            machine.etat = 'maintenance'    
    if type_materiel:
        machines = machines.filter(type_materiel=type_materiel)
    context = {
        'machines' : machines,
        'type_materiel' : type_materiel,
        'date_m' : date_m,
        
    }
    print(date_m)
    return render(request,'computerApp/liste_machines.html',context)

#vu liste personnel
@login_required
def liste_personnels(request):
    personnels = Personnel.objects.all()
    context = {
        'personnels' : personnels,
    }
    return render(request,'computerApp/liste_personnels.html',context)

# vu detail machine
@login_required
def machine_detail_view(request,pk):
    machine = get_object_or_404(Machine,id=pk)
    context = {'machine':machine}
    return render(request,'computerApp/machine_detail.html',context)

#vu ajout machine
@login_required
def machine_add_form(request):
    if request.method == 'POST' : 
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(
                nom_m = form.cleaned_data['nom_m'],
                lieu_infrastructure = form.cleaned_data['lieu_infrastructure'],
                maintenanceDate = (form.cleaned_data['maintenanceDate']),
                type_materiel = form.cleaned_data['type_materiel']
                )
            new_machine.save()
            messages.success(request, "La machine a été ajoutée avec succès.")
            return redirect('machines')
        
    else :
        form = AddMachineForm()
    context ={'form':form}
    return render(request,'computerApp/machine_add.html',context)

#vu suppression machine
@login_required
def machine_delete_form(request):
    if request.method == 'POST':
        form = DeleteMachineForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            phrase_confirmation = form.cleaned_data['phrase_confirmation']
            machine = Machine.objects.filter(id=id).first()
            if machine and phrase_confirmation == "Je confirme la suppression de la machine":
                machine.delete()
                return redirect('machines')
            else:
                error_msg = "ID inexistant ou phrase de confirmation invalide."
                context = {'form': form, 'error_msg': error_msg}
                return render(request, 'computerApp/machine_del.html', context)
    else:
        form = DeleteMachineForm()
    context = {'form': form}
    return render(request, 'computerApp/machine_del.html', context)

#vu du detail d'un personnel
@login_required
def personnel_detail_view(request,pk):
    personnel = get_object_or_404(Personnel,id=pk)
    context = {"personnel":personnel}
    return render(request,'computerApp/personnel_detail.html',context)

# vu ajout personnel
@login_required
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

#vu suppression personnel
@login_required
def personnel_delete_form(request):
    if request.method == 'POST':
        form = DeletePersonnelForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            phrase_confirmation = form.cleaned_data['phrase_confirmation']
            personnel = Personnel.objects.filter(id=id).first()
            if personnel and phrase_confirmation == "Je confirme la suppression de l utilisateur":
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

#vu infrastructure
@login_required
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

@login_required
def check_ip(request):
    map = None
    if request.method == 'POST':
        form = IPAddressForm(request.POST)
        if form.is_valid():
            ip_address = form.cleaned_data['ip_address']
            try:
                #verification de si c'est une IP
                ipaddress.ip_address(ip_address)
                is_valid = True

                #connexion avec la clef API
                apiKey = 'bdc_5b446486aeaf4a95a7829e947b329442'
                client = bigdatacloudapi.Client(apiKey)
                
                #retour de la requete 
                resultObject, httpResponseCode = client.getIpGeolocationFull({"ip": ip_address})
                value = resultObject

                #affichage du resultat de value sous la forme d'une carte
                latitude = value['location']['latitude']
                longitude = value['location']['longitude']
                map = folium.Map(location=[latitude, longitude], zoom_start=10)
                folium.Marker([latitude, longitude]).add_to(map)
#gestion des différentes erreurs pouvant arriver
            except ValueError:
                is_valid = False
                map = None
        else:
            is_valid = False
            map = None
    else:
        form = IPAddressForm()
        is_valid = None
        
    if map is not None:
        map_html = map._repr_html_()
    else:
        map_html = None

    context = {
        'form': form,
        'is_valid': is_valid,
        'map': map_html,
    }

    return render(request, 'computerApp/feature.html', context)

#vu connexion
def login_views(request):
    return LoginView.as_view(template_name='computerApp/login.html',redirect_authenticated_user=True)(request)

#vu deconnexion  
def logout_views(request):
    return LogoutView.as_view(template_name='computerApp/logout.html')(request)

#vu maintenance
def maintenance(request):
    temp_maintenance = request.GET.get('type')
    if temp_maintenance == 'a venir':
        maintenances = Machine.objects.filter(maintenanceDate__gte=timezone.now()).order_by('maintenanceDate')
    elif temp_maintenance == 'anciennes':
        maintenances = Machine.objects.filter(maintenanceDate__lt=timezone.now()).order_by('-maintenanceDate')
    else:
        maintenances = Machine.objects.none()

    context = {
        'maintenances' : maintenances,
    }
    
    return render(request, 'computerApp/maintenance.html', context)
    
 
