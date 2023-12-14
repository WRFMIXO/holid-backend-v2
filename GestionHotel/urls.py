from django.urls import path
from .views import HotelInformationsView

urlpatterns = [
    path('hotelinfo/', HotelInformationsView.as_view(), name='hotel-informations'),
]