from django.shortcuts import render
from rest_framework import generics
from .serializers import HotelInfosSerializer
from django.http import JsonResponse
from .models import HotelInformations

# Create your views here.
class HotelInformationsView(generics.ListCreateAPIView):
    queryset = HotelInformations.objects.all()
    serializer_class = HotelInfosSerializer