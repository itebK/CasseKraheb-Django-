from rest_framework import serializers
from .models import Marque, Modele, PieceDetachee, ZonePiece

class MarqueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Marque
        fields = ('libelle',)
        #field = '__all__'
    
class ModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modele
        fields = ('libelle',)
        
class FullModeleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modele
        fields = ('libelle','image')
        
class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonePiece
        fields = ('libelle',)
        
class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceDetachee
        fields = ('libelle',)
