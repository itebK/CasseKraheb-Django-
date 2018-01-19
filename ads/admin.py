from django.contrib import admin
from .models import Ads
from django.utils.text import Truncator

class AdsAdmin(admin.ModelAdmin):
   list_display   = ('type','compte', 'modele', 'piece', 'description','prix', 'ville', 'dateAnnonce')
   list_filter    = ('type','piece',)
   date_hierarchy = 'dateAnnonce'
   ordering       = ('dateAnnonce', )
   search_fields  = ('type', 'piece')

admin.site.register(Ads, AdsAdmin)
