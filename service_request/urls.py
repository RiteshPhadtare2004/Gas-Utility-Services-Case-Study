from django.urls import path
from . import views
from .views import track_requests

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/<int:pk>/', views.track_request, name='track_request'),
    path('track_request/', track_requests, name='track_request')
]
