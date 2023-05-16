from django.db import models
from datetime import datetime
from django.core.validators import EmailValidator
# Create your models here.

class Machine(models.Model):
    TYPE = (
        ('PC' , ('PC − Run windows ')),
        ('Mac',('MAc − Run MacOS')),
        ('Serveur',('Serveur −Simple Server to deploy virtual machines')),
        ('Switch',('Switch − To maintains and connect servers')),
        ('Routeur',('Routeur - To maintains and connect servers'))
    )

    id = models.AutoField( primary_key=True,editable=False)
    nom = models.CharField(max_length = 200 )
    maintenanceDate = models.DateField(default=datetime.now())
    mach = models.CharField(max_length=32,choices=TYPE,default='PC')
    def __str__(self):
        return str(self.id) + "->" + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

class Personnel(models.Model):
    id = models.AutoField( primary_key=True,editable=False)
    civilite = models.CharField(default='Indéfini',max_length= 13 )
    prenom = models.CharField(max_length = 200 ,)
    nom = models.CharField(max_length = 200 ,)
    email = models.CharField(max_length=50, validators=[EmailValidator(message="Veuillez entrer une adresse email valide.")])    
    poste = models.CharField(max_length = 200 ,)
    def __str__(self):
        return str(self.id) + "->" + self.nom + str(self.id) + "->" + self.prenom + str(self.id) + "->" + self.email + str(self.id) + "->" + self.poste
    def get_name(self):
        return str(self.id) + " " + self.nom +" " + self.prenom +" " + self.email +" " + self.poste