# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^marque/', views.MarqueList.as_view(), name="marque"),
    url(r'^modele/', views.ModeleList.as_view(), name="modele"),
    url(r'^modele-complet/', views.FullModeleList.as_view(), name="modele-complet"),
    url(r'^tout-les-modeles/', views.ModeleListAll.as_view(), name="modeleAll"),
    url(r'^piece/', views.PieceListAll.as_view(), name="piece"),
    url(r'^zone/', views.PieceList.as_view(), name="zone"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

"""
    url(r'^afficher/(?P<id_annonce>[0-9]+)$', views.ads_afficher, name="afficher"),
    url(r'^afficher-tout$', views.ads_afficher_all, name="afficher_all"),
    url(r'^ajouter$', views.ads_ajouter, name="ajouter_annonce"),
    url(r'^modifier/(?P<id_annonce>[0-9]+)$', views.ads_modifier, name="modifier_annonce"),
    url(r'^modele/(?P<modele>[a-z]+)$', views.ads_rechercher_modele, name="modele"),
    url(r'^zone/(?P<zone>[a-z]+)$', views.ads_rechercher_zone, name="zone"),
    url(r'^piece/(?P<piece>[a-z]+)$', views.ads_rechercher_piece, name="piece"),
    url(r'^supprimer/(?P<id_annonce>[0-9]+)$', views.ads_suprimer, name="supprimer_annonce"),
    
"""