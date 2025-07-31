from django.shortcuts import render, get_object_or_404, redirect
from .models import Club
#from users.models import Login
from django.contrib.auth.decorators import login_required


@login_required
def join_club(request, club_id):
    club = get_object_or_404(Club, id_club=club_id)

    if request.method == 'POST':
        if request.user not in club.members.all():
            club.members.add(request.user)
        return redirect('club_detail', club_id=club.id_club)
    
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

def join_club(request, club_id):
    if request.method == 'POST':
        if request.user.is_authenticated:  
            club = get_object_or_404(Club, id_club=club_id)
            club.members.add(request.user) 
            return redirect('club_detail', club_id=club.id_club)