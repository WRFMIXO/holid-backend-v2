# serializers.py
from rest_framework import serializers
from .models import Service

class CreateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ReadServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class UpdateServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DeleteServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
