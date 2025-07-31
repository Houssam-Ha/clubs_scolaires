from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('1', 'Member'),
        ('2', 'Encadrant'),
    ]
    
    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        default='1'
    )
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"