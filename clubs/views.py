from django.shortcuts import render, get_object_or_404, redirect
from .models import Club
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def join_club(request, club_id):
    club = get_object_or_404(Club, id_club=club_id)
    
    if request.method == 'POST':
        if request.user not in club.members.all():
            club.members.add(request.user)
            messages.success(request, f'You have successfully joined {club.nom_club}!')
        return redirect('club', club_id=club.id_club)  # This should match your URL pattern
    
    return redirect('clubs')
    
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

 
