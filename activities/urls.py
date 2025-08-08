from django.urls import path
from . import views

urlpatterns = [
    path("", views.activities, name="activities"),
    path("activity/", views.activity, name="activity"),
    path("my-activities/", views.my_activities, name="my_activities"),
    path('join/<int:activity_id>/', views.join_activity, name='join_activity'),
    path('leave/<int:activity_id>/', views.leave_activity, name='leave_activity'),
    path('create/', views.create_activity, name='create_activity'),
]