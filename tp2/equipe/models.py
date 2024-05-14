from django.db import models

# Create your models here.

class Equipe(models.Model):
    nom = models.CharField(max_length=50)
    nbr_joueurs = models.IntegerField(blank=False)
    ville_assignee = models.CharField(max_length=50)
    date_creation = models.CharField(max_length=50)
    niveau = models.ForeignKey("niveau", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = (f"Le club {self.nom} à été créé le {self.date_creation} dans la ville "
                  f"{self.ville_assignee} et elle y compte {self.nbr_joueurs} joueurs")
        return chaine

    def dico(self):
        return {"nom": self.nom, "nbr_joueurs": self.nbr_joueurs, "ville_assignee": self.ville_assignee, "date_creation": self.date_creation, "niveau": self.niveau}

class Niveau(models.Model):
    avis = models.CharField(max_length=100 , blank=False)
    particularite = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.avis

    def dico(self):
        return {"avis": self.avis, "particularite": self.particularite}