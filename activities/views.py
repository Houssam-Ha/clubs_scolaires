from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Activity
from clubs.models import Club

def activities(request):
    """Display all activities with filtering options"""
    activities_list = Activity.objects.select_related('club', 'created_by').prefetch_related('participants')
    
    # Filter by status
    status_filter = request.GET.get('status', '')
    if status_filter:
        activities_list = activities_list.filter(status=status_filter)
    
    # Filter by activity type
    type_filter = request.GET.get('type', '')
    if type_filter:
        activities_list = activities_list.filter(activity_type=type_filter)
    
    # Filter by club
    club_filter = request.GET.get('club', '')
    if club_filter:
        activities_list = activities_list.filter(club_id=club_filter)
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        activities_list = activities_list.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(club__nom_club__icontains=search_query)
        )
    
    # Order activities
    activities_list = activities_list.order_by('start_date', 'start_time')
    
    # Statistics
    upcoming_count = Activity.objects.filter(status='upcoming').count()
    ongoing_count = Activity.objects.filter(status='ongoing').count()
    featured_count = Activity.objects.filter(is_featured=True).count()
    
    # Get all clubs for filter dropdown
    clubs = Club.objects.filter(active=True).order_by('nom_club')
    
    context = {
        'activities': activities_list,
        'clubs': clubs,
        'upcoming_count': upcoming_count,
        'ongoing_count': ongoing_count,
        'featured_count': featured_count,
        'activity_types': Activity.ACTIVITY_TYPE_CHOICES,
        'status_choices': Activity.STATUS_CHOICES,
        'current_filters': {
            'status': status_filter,
            'type': type_filter,
            'club': club_filter,
            'search': search_query,
        }
    }
    return render(request, "activities/activities.html", context)

def activity(request):
    """Display single activity details"""
    activity_id = request.GET.get('id')
    if activity_id:
        activity = get_object_or_404(Activity, id_activity=activity_id)
    else:
        activity = None
    
    context = {
        'activity': activity,
        'user_registered': activity and request.user.is_authenticated and request.user in activity.participants.all(),
        'can_register': activity and activity.registration_required and not activity.is_full and activity.status == 'upcoming',
    }
    return render(request, "activities/activity.html", context)

@login_required
def my_activities(request):
    """Display user's joined activities"""
    user_activities = Activity.objects.filter(
        participants=request.user
    ).select_related('club', 'created_by').order_by('-start_date', '-start_time')
    
    # Separate by status
    upcoming_activities = user_activities.filter(status='upcoming')
    ongoing_activities = user_activities.filter(status='ongoing')
    completed_activities = user_activities.filter(status='completed')
    
    context = {
        'upcoming_activities': upcoming_activities,
        'ongoing_activities': ongoing_activities,
        'completed_activities': completed_activities,
        'total_activities': user_activities.count(),
    }
    return render(request, "activities/my_activities.html", context)

@login_required
def join_activity(request, activity_id):
    """Join an activity"""
    activity = get_object_or_404(Activity, id_activity=activity_id)
    
    if request.method == 'POST':
        if request.user not in activity.participants.all():
            if not activity.is_full:
                activity.participants.add(request.user)
                messages.success(request, f'You have successfully joined "{activity.title}"!')
            else:
                messages.error(request, 'Sorry, this activity is full.')
        else:
            messages.info(request, 'You are already registered for this activity.')
        
        return redirect(f'/activities/activity/?id={activity.id_activity}')
    
    return redirect('activities')

@login_required
def leave_activity(request, activity_id):
    """Leave an activity"""
    activity = get_object_or_404(Activity, id_activity=activity_id)
    
    if request.method == 'POST':
        if request.user in activity.participants.all():
            activity.participants.remove(request.user)
            messages.success(request, f'You have left "{activity.title}".')
        else:
            messages.info(request, 'You are not registered for this activity.')
        
        return redirect(f'/activities/activity/?id={activity.id_activity}')
    
    return redirect('activities')

@login_required
def create_activity(request):
    """Create new activity - Admin only"""
    # Check if user has permission (you can customize this check)
    if not request.user.user_type in ['2', '3']:  # Encadrant or Administration
        messages.error(request, 'You do not have permission to create activities.')
        return redirect('activities')
    
    if request.method == 'POST':
        try:
            # Get form data
            title = request.POST.get('title')
            description = request.POST.get('description')
            activity_type = request.POST.get('activity_type')
            club_id = request.POST.get('club')
            start_date = request.POST.get('start_date')
            start_time = request.POST.get('start_time')
            end_date = request.POST.get('end_date')
            end_time = request.POST.get('end_time')
            location = request.POST.get('location')
            max_participants = request.POST.get('max_participants', 50)
            registration_required = request.POST.get('registration_required') == 'on'
            requirements = request.POST.get('requirements', '')
            is_featured = request.POST.get('is_featured') == 'on'
            
            # Get club
            club = get_object_or_404(Club, id_club=club_id)
            
            # Create activity
            activity = Activity.objects.create(
                title=title,
                description=description,
                activity_type=activity_type,
                club=club,
                start_date=start_date,
                start_time=start_time,
                end_date=end_date,
                end_time=end_time,
                location=location,
                max_participants=int(max_participants),
                registration_required=registration_required,
                requirements=requirements,
                is_featured=is_featured,
                created_by=request.user,
                status='upcoming'
            )
            
            # Handle image upload
            if 'image' in request.FILES:
                activity.image = request.FILES['image']
                activity.save()
            
            messages.success(request, f'Activity "{title}" created successfully!')
            return redirect('activity') + f'?id={activity.id_activity}'
            
        except Exception as e:
            messages.error(request, f'Error creating activity: {str(e)}')
    
    # Get clubs for dropdown
    clubs = Club.objects.filter(active=True).order_by('nom_club')
    
    context = {
        'clubs': clubs,
        'activity_types': Activity.ACTIVITY_TYPE_CHOICES,
    }
    return render(request, "activities/create_activity.html", context)