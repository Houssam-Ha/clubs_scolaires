from django.contrib import admin
from .models import Club

class ClubAdmin(admin.ModelAdmin):
    list_display = ('nom_club', 'date_creation', 'active')
    filter_horizontal = ('members',)  

admin.site.register(Club, ClubAdmin)
