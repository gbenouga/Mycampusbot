from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#liste de la semaine
class Semaine_list(models.Model):
   jour_id = models.AutoField(primary_key=True)
   jour = models.CharField(max_length=255)
   
#utilisateur
class User(models.Model):
    id = models.AutoField(primary_key=True)
    telegram_id = models.CharField(max_length=255, unique=True)
    nom_bot = models.CharField(max_length=50)
    nom_utilisateur = models.CharField(max_length=255)
    nom_utilisateur = models.CharField(max_length=200)
    prenom_utilisateur = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'utilisateur'
        verbose_name_pluriel = 'utilisateurs'
    
class Recette(models.Model):
    id = models.AutoField(primary_key=True)
    jour = models.ForeignKey(Semaine_list, on_delete=models.CASCADE)
    entree = models.CharField(max_length=255,)
    plat_de_resistance = models.CharField(max_length=255)
    dessert = models.CharField(max_length=255)
        
    def __str__(self):
        return "Recette du {self.jour} : {self.entree} + {self.plat_de_resistance} + {self.dessert})"
    
class Horaire(models.Model):
    horaire_id  = models.AutoField(primary_key=True)
    heure = models.CharField(null=False, blank=False)


class Localite(models.Model):
    localite_id = models.AutoField(primary_key=True)
    localite = models.CharField(null=False)
    
class Bus_numero(models.Model):
    id_numero = models.AutoField(primary_key=True)
    numero = models.CharField(null=False)
class Bus_Horaire(models.Model):
    bus_horaire_id = models.AutoField(primary_key=True)
    horaireid = models.ForeignKey(Horaire, on_delete=models.CASCADE)
    localite_id = models.ForeignKey(Localite, on_delete=models.CASCADE)
    bus_no = models.ForeignKey(Bus_numero, on_delete=models.CASCADE)
