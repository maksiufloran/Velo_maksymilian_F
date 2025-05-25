from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Hit
from .serializers import HitSerializer

# Lista 20 najnowszych hitów + możliwość dodania nowego
class HitListCreateView(generics.ListCreateAPIView):
    queryset = Hit.objects.all().order_by('-created_at')[:20] # [:20] to sort descending
    serializer_class = HitSerializer

# Pobranie, edycja lub usunięcie hitu po title_url
class HitDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'title_url'  # czyli szukamy po title_url, nie po id
    queryset = Hit.objects.all()
    serializer_class = HitSerializer