from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('1', 'Member'),
        ('2', 'Encadrant'),
        ('3', 'Administration')
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        default='1'
    )
    
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"