from django.db import models
from datetime import datetime
from django.core.validators import EmailValidator

# Create your models here.

class Machine(models.Model):
    TYPE = (
        ('PC' , ('PC')),
        ('Mac',('MAc')),
        ('Serveur',('Serveur')),
        ('Switch',('Switch')),
        ('Routeur',('Routeur'))
    )

    Infrastructure = (
        ('Poitiers',('Poitiers')),
        ('Marseille',('Marseille')),
        ('Châtellerault',('Châtellerault')),
    )

    id = models.AutoField( primary_key=True,editable=False)
    nom = models.CharField(max_length = 200 )
    maintenanceDate = models.DateField(default=datetime.now())
    type_materiel = models.CharField(max_length = 40,choices=TYPE,default='PC')
    lieu_infrastructure = models.CharField(max_length = 60, choices=Infrastructure,default='Marseille')

class Personnel(models.Model):
    Poste = (
        ('Ingénieur en sécurité informatique', 'Ingénieur en sécurité informatique'),
        ('Administrateur système', 'Administrateur système'),
        ('Administrateur réseau', 'Administrateur réseau'),
        ('Technicien support informatique', 'Technicien support informatique'),
        ("Analyste en systèmes d'information", "Analyste en systèmes d'information"),
        ("Développeur d'applications", "Développeur d'applications"),
        ('Responsable de la gestion des données', 'Responsable de la gestion des données'),
    )

    Infrastructure = (
        ('Poitiers', 'Poitiers'),
        ('Marseille', 'Marseille'),
        ('Châtellerault', 'Châtellerault'),
    )

    Civilite = (
        ('Homme',('Homme')),
        ('Femme',('Femme')),
        ('Indéfini',('Indéfini')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    civilite = models.CharField(max_length = 32, choices=Civilite,default='Indéfini')
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    email = models.CharField(max_length=50,validators=[EmailValidator(message="Veuillez entrer une adresse email valide.")])
    poste = models.CharField(max_length = 40, choices=Poste,default='Employer')
    infrastructure = models.CharField(max_length = 60,choices=Infrastructure, default='Marseille')
