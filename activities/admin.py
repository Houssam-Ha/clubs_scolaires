from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'club', 'activity_type', 'start_date', 'start_time', 'status', 'participants_count', 'created_by')
    list_filter = ('activity_type', 'status', 'club', 'start_date', 'is_featured')
    search_fields = ('title', 'description', 'club__nom_club', 'location')
    filter_horizontal = ('participants',)
    date_hierarchy = 'start_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'activity_type', 'club', 'image')
        }),
        ('Schedule', {
            'fields': ('start_date', 'start_time', 'end_date', 'end_time', 'location')
        }),
        ('Registration', {
            'fields': ('registration_required', 'max_participants', 'registration_deadline', 'requirements')
        }),
        ('Management', {
            'fields': ('status', 'is_featured', 'created_by', 'participants')
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
    
    def participants_count(self, obj):
        return obj.participants.count()
    participants_count.short_description = 'Participants'
    
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new activity
            obj.created_by = request.user
        super().save_model(request, obj, form, change)