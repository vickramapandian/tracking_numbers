# tracking/urls.py
from django.urls import path
from .views import TrackingNumberGenerateView

urlpatterns = [
    path('generate/', TrackingNumberGenerateView.as_view(), name='generate-tracking-number'),
]
