from django.urls import path
from . import views

urlpatterns = [
    path("", views.clubs, name="clubs"),
    path("club/", views.club, name="club"),
    path('join/<int:club_id>/', views.join_club, name='join__club'),
]