from django.db import models


# class Login(models.Model):
#     USER_TYPE_CHOICES = [
#         ('1', 'Member'),
#         ('2', 'Encadrant'),
#     ]

#     username = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=30, null=True)
#     password = models.CharField(max_length=50)
#     email = models.EmailField(max_length=100, unique=True, null=True)

#     user_type = models.CharField(
#         max_length=1,  
#         choices=USER_TYPE_CHOICES,
#         default='1'    
#     )

#     def __str__(self):
#         return f"{self.username} ({self.get_user_type_display()})"



