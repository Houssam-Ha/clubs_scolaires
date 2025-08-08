from django.db import models
from django.conf import settings
from clubs.models import Club

class Activity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('meeting', 'Meeting'),
        ('workshop', 'Workshop'),
        ('event', 'Event'),
        ('competition', 'Competition'),
        ('training', 'Training'),
        ('social', 'Social Activity'),
        ('community', 'Community Service'),
        ('trip', 'Field Trip'),
    ]
    
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    id_activity = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPE_CHOICES, default='meeting')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='activities')
    
    # Date and Time
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    
    # Location
    location = models.CharField(max_length=200)
    
    # Capacity and Registration
    max_participants = models.PositiveIntegerField(default=50)
    registration_required = models.BooleanField(default=True)
    registration_deadline = models.DateTimeField(blank=True, null=True)
    
    # Status and Management
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_activities')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='joined_activities', blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Additional fields
    image = models.ImageField(upload_to='activities/%Y/%m/%d/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    requirements = models.TextField(blank=True, help_text="Any special requirements or things to bring")
    
    class Meta:
        verbose_name_plural = "Activities"
        ordering = ['start_date', 'start_time']
    
    def __str__(self):
        return f"{self.title} - {self.club.nom_club}"
    
    @property
    def is_full(self):
        return self.participants.count() >= self.max_participants
    
    @property
    def spots_remaining(self):
        return self.max_participants - self.participants.count()
    
    @property
    def duration_hours(self):
        from datetime import datetime, timedelta
        start = datetime.combine(self.start_date, self.start_time)
        end = datetime.combine(self.end_date, self.end_time)
        duration = end - start
        return duration.total_seconds() / 3600