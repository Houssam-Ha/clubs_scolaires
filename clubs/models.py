from django.db import models

# Create your models here.
class Club(models.Model):
    id_club = models.AutoField(primary_key=True)
    nom_club = models.CharField(max_length=20)
    description = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    logo = models.ImageField(upload_to='logo/%Y/%m/%d/')
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.nom_club
    # class Meta:
    #     verbose_name = 'Club'
    #     verbose_name_plural = 'Clubs'
    #     ordering = ['nom_club']
