from django.db import models
from comptes.models import Compte

def upload_location(instance, filename):
    return "img/{0}/{1}".format(instance.id, filename)

class Ads(models.Model):
    
    description = models.TextField(null=True)
    image = models.FileField(upload_to = upload_location,
                             null=True,
                             blank=True)
    prix = models.FloatField(null=True)
    dateAnnonce = models.DateTimeField(auto_now_add=True, null=True,
                                verbose_name="date annonce")
    type = models.CharField(max_length=10)
    compte = models.ForeignKey('comptes.Compte', on_delete=models.CASCADE,null=True,)
    ville = models.ForeignKey('Ville', on_delete=models.CASCADE,null=True,)
    modele = models.ForeignKey('Modele', on_delete=models.CASCADE,null=True,)
    piece = models.ForeignKey('PieceDetachee', on_delete=models.CASCADE,null=True,)
    
    def __str__(self):
        return self.compte.username

class ZonePiece(models.Model):
    
    libelle = models.CharField(max_length=1000)
    image = models.FileField(null=True)
    
    def __str__(self):
        return self.libelle

class PieceDetachee(models.Model):
    
    libelle = models.CharField(max_length=1000)
    zonePiece = models.ForeignKey('ZonePiece', on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.libelle
    
class Ville(models.Model):
    
    libelle = models.CharField(max_length=1000)
    codeGouvernorat = models.ForeignKey('Gouvernorat', on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.libelle
    
class Gouvernorat(models.Model):
    
    libelle = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.libelle
    
class Modele(models.Model):
    
    libelle = models.CharField(max_length=1000)
    image = models.FileField(null=True)
    codeMarque = models.ForeignKey('Marque', on_delete=models.CASCADE,)
    
    def __str__(self):
        return self.libelle
    
class Marque(models.Model):
    
    libelle = models.CharField(max_length=1000)
    image = models.FileField(null=True)
    
    def __str__(self):
        return self.libelle