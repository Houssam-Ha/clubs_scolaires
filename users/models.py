from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('1', 'Member'),
        ('2', 'Encadrant'),
        ('3', 'Administration')
    ]
    
    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        default='1'
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

class male_or_femelle(AbstractUser):
    USER_TYPE = [
        ('1', 'male'),
        ('2', 'femelle'),
    ]
    
    user_sex = models.CharField(
        max_length=1,
        choices=USER_TYPE,
    )
    
    def __str__(self):
        return f"{self.username} ({self.user_sex_display()})"
    