from django.shortcuts import render, get_object_or_404
from .models import Club

def clubs(request):
    clubs = Club.objects.order_by('nom_club')
    active_clubs_count = Club.objects.filter(active=True).count()
    
    context = {
        'clubs': clubs,
        'active_clubs_count': active_clubs_count,
    }
    return render(request, "clubs/clubs.html", context)

def club(request):
    club_id = request.GET.get('id')
    if club_id:
        club = get_object_or_404(Club, id_club=club_id)
    else:
        club = None
    
    context = {
        'club': club,
    }
    return render(request, "clubs/club.html", context)