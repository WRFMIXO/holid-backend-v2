from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .models import CustomUser
from .serializers import CustomUserSerializer, CreateUserSerializer
from django.http import JsonResponse

class UserListView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serialized_users = CustomUserSerializer(users, many=True).data

        print("Serialized Users:", serialized_users)        
        # Extraire les colonnes de la première instance sérialisée (si disponible)
        columns = []
        if serialized_users:
            columns = [{"field": key, "headerName": key.upper(), "width": 200} for key in serialized_users[0].keys()]

        data = {
            "columns": columns,
            "rows": serialized_users
        }

        return JsonResponse(data)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serialized_users = CustomUserSerializer(users, many=True).data

        print("Serialized Users:", serialized_users)        
        # Extraire les colonnes de la première instance sérialisée (si disponible)
        columns = []
        if serialized_users:
            columns = [{"field": key, "headerName": key.upper(), "width": 200} for key in serialized_users[0].keys()]

        data = {
            "columns": columns,
            "rows": serialized_users
        }

        return JsonResponse(data)

class UserLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200 and request.user.is_authenticated:
            user = self.request.user
            serialized_user = CustomUserSerializer(user).data

            columns = [{"field": key, "headerName": key.upper(), "width": 200} for key in serialized_user.keys()]

            data = {
                "columns": columns,
                "rows": [serialized_user]
            }

            return JsonResponse(data)

        return response

class UserLogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Utilisez "permission_classes" au lieu de "permissions_classes"

    def post(self, request):
        return Response(status=status.HTTP_200_OK)
    
class UserRefreshTokenView(TokenRefreshView):  # Corrigez le nom de la classe
    pass

class UserVerifyTokenView(TokenVerifyView):
    pass

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)