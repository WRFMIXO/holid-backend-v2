from rest_framework import serializers
from .models import HotelInformations

class HotelInfosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelInformations
        fields = "__all__"
