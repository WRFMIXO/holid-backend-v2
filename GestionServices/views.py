# views.py
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Service
from django.http import JsonResponse
from .serializers import CreateServiceSerializer, ReadServiceSerializer, UpdateServiceSerializer, DeleteServiceSerializer
from rest_framework.permissions import IsAuthenticated

class CreateServiceView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_classes = [IsAuthenticated]

class ListServiceViewDetailled(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ReadServiceSerializer

    def get(self, request, *args, **kwargs):
        service = Service.objects.all()
        serialized_services = ReadServiceSerializer(service, many=True).data

        print("Serialized Services:", serialized_services)        
        # Extraire les colonnes de la première instance sérialisée (si disponible)
        columns = []
        if serialized_services:
            columns = [{"field": key, "headerName": key.upper(), "width": 200} for key in serialized_services[0].keys()]

        data = {
            "columns": columns,
            "rows": serialized_services
        }

        return JsonResponse(data)
    
class ListServicesView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ReadServiceSerializer

class RetrieveUpdateServiceView(RetrieveUpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = UpdateServiceSerializer
    permission_classes = [IsAuthenticated]

class DeleteServiceView(DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = DeleteServiceSerializer
    permission_classes = [IsAuthenticated]
