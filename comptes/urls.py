from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^connexion$', views.user_signin, name="connexion"),
    url(r'^inscription$', views.user_signup, name="inscription"),
    url(r'^deconnecter$', views.user_logout, name="deconnexion"),
    url(r'^valider', views.user_validation, name="validation"),
    url(r'^modifier$', views.user_update, name="modification"),
    url(r'^(\d+)$', views.user_profile, name="compte"),

]
