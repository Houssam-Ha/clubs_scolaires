from django.shortcuts import render
from .models import Club
# Create your views here.
def clubs(request):
    return render(request, "clubs/clubs.html", {"clubs": Club.objects.all()})

def club(request):
    return render(request, "clubs/club.html")