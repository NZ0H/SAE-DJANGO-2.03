from django import forms
from django.core.exceptions import ValidationError
from .models import Machine,Personnel

class AddMachineForm (forms.Form ) :
    nom = forms.CharField (required = True ,label = 'Nom de la machine' )
    def clean_nom(self) :
        data = self.cleaned_data ["nom"]
        if len(data) > 15 :
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data
    def clean_date_maintenace(self):
        pass


class DeleteMachineForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom de la machine à supprimer')
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        try:
            machine = Machine.objects.get(nom=data)
        except Machine.DoesNotExist:
            raise forms.ValidationError("Cette machine n'existe pas")
        return data


class AddPersonnelForm (forms.Form ) :
    nom = forms.CharField (required = True ,label = "Nom de l'employé" )
    prenom = forms.CharField (required = True ,label = "Prenom de l'employé" )
    email = forms.CharField (required = True ,label = "Prenom de l'employé" )
    poste = forms.CharField (required = True ,label = "Prenom de l'employé" )
    civilite = forms.CharField (required = True ,label = "Prenom de l'employé" )

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
        if len(data) > 15 :
            raise ValidationError(("Erreur de format pour le champ poste"))
        return data
    def clean_email(self):
        data = self.cleaned_data ["email"]
        if len(data) > 50 :
            raise ValidationError(("Erreur de format pour le champ email"))
        return data
    def clean_civilite(self):
        data = self.cleaned_data ["civilite"]
        if data not in ['Madame', 'Monsieur']:
            raise ValidationError(("Erreur de format pour le champ civilité"))
        return data
    
class DeletePersonnelForm(forms.Form):
    id = forms.CharField(required=True, label="Nom de l'employé à supprimer")
    phrase_confirmation = forms.CharField(label='Confirmez la suppression en écrivant "supprimer"')

    def clean_id(self):
        data = self.cleaned_data["id"]
        personnel = Personnel.objects.get(id=data)
        return data
   