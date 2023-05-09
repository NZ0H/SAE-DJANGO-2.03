from django.db import models

# Create your models here.

class Machine(models.Model):
    id = models.AutoField(
        primary_key=True,
        editable=False
    )
    nom = models.CharField(
        max_length = 200 ,
        )
    def __str__(self):
        return str(self.id) + "->" + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom

class Personnel(models.Model):
    css = models.CharField(
        primary_key=True,
        default=0,
        max_length= 13
        )

    prenom = models.CharField(
        max_length = 200 ,
    )

    nom = models.CharField(
        max_length = 200 ,
        )

    def __str__(self):
        return str(self.css) + "->" + self.nom + str(self.css) + "->" + self.prenom

    def get_name(self):
        return str(self.css) + " " + self.nom +" " + self.prenom