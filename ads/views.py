# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Marque, Modele
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarqueSerializer 
from django.template.context_processors import request
from ads.models import PieceDetachee, ZonePiece
from ads.serializers import *
from django.core import serializers

def home(request):
    marque = Marque.objects.all()
    zone = ZonePiece.objects.all()
    
    return render(request, 'ads/index.html', {'marques':marque, 'zones':zone})

class MarqueList(APIView):
    
    def get(self, request):
        marque = Marque.objects.all()
        serializer = MarqueSerializer(marque, many=True)
        return Response(serializer.data)

class ModeleList(APIView):
    
    def get(self, request):  
        id_marque = Marque.objects.values_list('id', flat=True).filter(libelle=request.GET.get('marque'))
        modele = Modele.objects.filter(codeMarque=id_marque)
        serializer = ModeleSerializer(modele, many=True)
        return Response(serializer.data)

class FullModeleList(APIView):
    
    def get(self, request):
        id_marque = Marque.objects.values_list('id', flat=True).filter(libelle=request.GET.get('marque'))
        modele = Modele.objects.filter(codeMarque=id_marque)
        serializer = FullModeleSerializer(modele, many=True)
        return Response(serializer.data)

class ModeleListAll(APIView):
    
    def get(self, request):
        modele = Modele.objects.all()
        serializer = ModeleSerializer(modele, many=True)
        return Response(serializer.data)
    
class PieceList(APIView):
    
    def get(self, request):
        id_zone = ZonePiece.objects.values_list('id', flat=True).filter(libelle=request.GET.get('zone'))
        modele = PieceDetachee.objects.filter(zonePiece=id_zone)
        serializer = ZoneSerializer(modele, many=True)
        return Response(serializer.data)
    
class PieceListAll(APIView):
    
    def get(self, request):
        modele = PieceDetachee.objects.all()
        serializer = PieceSerializer(modele, many=True)
        return Response(serializer.data)











def ads_rechercher_marque(request):
    json =  ""
    return json


def ads_filter(reuest):
    json =  ""
    return json

def ads_afficher(request, id_annonce):
    return HttpResponse("ads_afficher")

def ads_afficher_all(request):
    return HttpResponse("ads_afficher_all")

def ads_ajouter(request):
    return HttpResponse("ads_ajouter")

def ads_modifier(request, id_annonce):
    return HttpResponse("ads_modifier")

def ads_suprimer(request, id_annonce):
    return HttpResponse("ads_suprimer")

def ads_rechercher_modele(request, modele):
    return HttpResponse("ads_rechercher_modele")

def ads_rechercher_zone(request, zone):
    return HttpResponse("ads_rechercher_zone")

def ads_rechercher_piece(request, zone):
    return HttpResponse("ads_rechercher_piece")