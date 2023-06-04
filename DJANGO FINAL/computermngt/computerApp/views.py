from django.shortcuts import render,get_object_or_404,redirect
from .models import Machine,Personnel
from .forms import AddMachineForm, DeleteMachineForm,AddPersonnelForm,DeletePersonnelForm,IPAddressForm

# module de login django
from django.contrib.auth.views import LoginView

# bibliotheque pour la feature
import folium
import ipaddress
import bigdatacloudapi



def index(request):
    machines = Machine.objects.all()
    personnels = Personnel.objects.all()
    context = {
        'machines' : machines,
        'personnels' : personnels,
    }
    return render(request,'index.html',context)

def liste_machines(request):
    machines = Machine.objects.all()
    type_materiel = request.GET.get('type')
    if type_materiel:
        machines = machines.filter(type_materiel=type_materiel)
    context = {
        'machines' : machines,
        'type_materiel' : type_materiel,
    }
    return render(request,'computerApp/liste_machines.html',context)

def liste_personnels(request):
    personnels = Personnel.objects.all()
    context = {
        'personnels' : personnels,
    }
    return render(request,'computerApp/liste_personnels.html',context)

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

def check_ip(request):
    map = None
    if request.method == 'POST':
        form = IPAddressForm(request.POST)
        if form.is_valid():
            ip_address = form.cleaned_data['ip_address']
            try:
                ipaddress.ip_address(ip_address)
                is_valid = True

                apiKey = 'bdc_5b446486aeaf4a95a7829e947b329442'
                client = bigdatacloudapi.Client(apiKey)
                
                resultObject, httpResponseCode = client.getIpGeolocationFull({"ip": ip_address})
                value = resultObject

                latitude = value['location']['latitude']
                longitude = value['location']['longitude']
                map = folium.Map(location=[latitude, longitude], zoom_start=10)
                folium.Marker([latitude, longitude]).add_to(map)

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

def login(request):
    return LoginView.as_view(
        template_name='computerApp/log.html',
        redirect_authenticated_user=True)(request)
      


    
 
