# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Compte(models.Model):
    
    compte = models.OneToOneField(User)
    #username
    #email
    #password
    #is_active
    #is_staff
    #is_superuser
    #last_login
    
    tel = models.CharField(max_length=15)
    
    def __str__(self):
        return "Compte de {0}".format(self.compte.username)