from django.db import models
from django.conf import settings

class Club(models.Model):
    id_club = models.AutoField(primary_key=True)
    nom_club = models.CharField(max_length=20)
    description = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    logo = models.ImageField(upload_to='logo/%Y/%m/%d/', null=True, blank=True)
    active = models.BooleanField(default=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='joined_clubs', blank=True)

    def __str__(self):
        return self.nom_club