from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.views import APIView
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

             # met à jour la date de dernière connexion
            user.last_login = timezone.now()
            user.save()

            # Active l'utilisateur sur la plateforme
            user.is_active = True
            user.save()

            role = "super_admin" if user.is_superuser else "regular_user"
            permissions = ["read", "write"]  # Vous devrez définir cela en fonction de votre logique d'autorisation

            data = {
                "access": str(response.data["access"]),
                "refresh": str(response.data["refresh"]),
                "role": role,
                "permissions": permissions,
                # Ajoutez d'autres informations dont vous avez besoin ici
            }

            return Response(data, status=status.HTTP_200_OK)

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
    
class ActiveUsers(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(is_active=True)
    
class InactiveUsers(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(is_active=False)

class AllUsers(generics.ListAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.all()
