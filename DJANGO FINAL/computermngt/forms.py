from django import forms
from django.core.exceptions import ValidationError
from .models import Machine,Personnel
from datetime import date
from random import random

class AddMachineForm (forms.Form ) :
    nom_m = forms.CharField (
        required = True ,
        label = 'Nom de la machine',
        widget=forms.TextInput(attrs={'size': '26'}))
    
    lieu_infrastructure = forms.ChoiceField(
        required=True,
        label='Infrastructure',
        choices=[('Poitiers', 'Poitiers'),
        ('Marseille', 'Marseille'),
        ('Châtellerault', 'Châtellerault'),],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    maintenanceDate = forms.CharField(
        required=True,
        label='Date de maintenance',
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}),
    )

    type_materiel = forms.ChoiceField (
        required = True ,
        label = 'Type de matériel',
        choices = [
            ('PC', ('PC')),
            ('Mac',('MAc')),
            ('Serveur',('Serveur')),
            ('Switch',('Switch')),
            ('Routeur',('Routeur')),],
        widget=forms.Select(attrs={'class': 'form-control'}))
   
    def clean_nom_m(self) :
        data = self.cleaned_data ["nom_m"]
        if len(data) > 15 :
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data
    
    def clean_maintenanceDate(self):
        data = self.cleaned_data["maintenanceDate"]
        return data
    
    def clean_lieu_infrastructure(self):
        data = self.cleaned_data ["lieu_infrastructure"]
        if len(data) > 15 :
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data
    
    def clean_type_materiel(self):
        data = self.cleaned_data ["type_materiel"]
        if len(data) > 15 :
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data
    
   

class DeleteMachineForm(forms.Form):
    id = forms.CharField(required=True, label="ID de la machine à supprimer")
    phrase_confirmation = forms.CharField(label='Confirmez la suppression en écrivant "Je confirme la suppression de la machine"')
    def clean_id(self):
        data = self.cleaned_data["id"]
        machine = Machine.objects.get(id=data)
        return data


class AddPersonnelForm (forms.Form ) :
    nom = forms.CharField (
        required = True ,
        label = "Nom de l'employé",
        widget=forms.TextInput(attrs={'size': '26'}))
    
    prenom = forms.CharField (
        required = True ,
        label = "Prenom de l'employé",
         widget=forms.TextInput(attrs={'size': '26'}) )
    
    email = forms.CharField (
        required = True ,
        label = "Email de l'employé",
        widget=forms.TextInput(attrs={'size': '26'}))
    
    poste = forms.ChoiceField (
        required = True ,
        label = "Poste de l'employé",
        choices= [('Ingénieur en sécurité informatique', ('Ingénieur en sécurité informatique')),
        ('Administrateur système', ('Administrateur système')),
        ('Administrateur réseau', ('Administrateur réseau')),
        ('Technicien support informatique', ('Technicien support informatique')),
        ("Analyste en systèmes d'information", ("Analyste en systèmes d'information")),
        ("Développeur d'applications", ("Développeur d'applications")),
        ('Responsable de la gestion des données', ('Responsable de la gestion des données')),],
        widget=forms.Select(attrs={'class': 'form-control'}))
    
    civilite = forms.ChoiceField (
        required = True ,
        label = "Civilite de l'employé",
        choices=[('Homme' , ('Homme')),('Femme',('Femme')),('Indéfini',('Indéfini')),],
        widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_nom(self) :
        data = self.cleaned_data ["nom"]
        if len(data) > 15 :
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data
    
    def clean_prenom(self):
        data = self.cleaned_data ["prenom"]
        if len(data) > 15 :
            raise ValidationError(("Erreur de format pour le champ prenom"))
        return data
    
    def clean_poste(self):
        data = self.cleaned_data ["poste"]
        if data not in ['Ingénieur en sécurité informatique','Administrateur système','Administrateur réseau','Technicien support informatique',"Analyste en systèmes d'information","Développeur d'applications",'Responsable de la gestion des données']:
            raise ValidationError(("Erreur de format pour le champ poste"))
        return data
    
    def clean_email(self):
        data = self.cleaned_data ["email"]
        if len(data) > 50 :
            raise ValidationError(("Erreur de format pour le champ email"))
        return data
    
    def clean_civilite(self):
        data = self.cleaned_data ["civilite"]
        if data not in ['Homme', 'Femme','Indéfini']:
            raise ValidationError(("Erreur de format pour le champ civilité"))
        return data
    

class DeletePersonnelForm(forms.Form):
    id = forms.CharField(required=True, label="Nom de l'employé à supprimer")
    phrase_confirmation = forms.CharField(label='Confirmez la suppression en écrivant : "Je confirme la suppression de la machine"')
    #poste = forms.ModelChoiceField(queryset=Personnel.Poste)
    def clean_id(self):
        data = self.cleaned_data["id"]
        personnel = Personnel.objects.get(id=data)
        return data
    
class IPAddressForm(forms.Form):
    ip_address = forms.GenericIPAddressField(label='Adresse IP',error_messages={'invalid': 'IP invalide, vérifiez votre requête.'})
