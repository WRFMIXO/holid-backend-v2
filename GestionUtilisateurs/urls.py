from django.urls import path
from .views import UserDetailView, UserListView, UserLoginView, UserLogoutView, UserRefreshTokenView, UserVerifyTokenView, CreateUserView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-details'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('refresh-token/', UserRefreshTokenView.as_view(), name='refresh-token'),
    path('verify-token/', UserVerifyTokenView.as_view(), name='verify-token'),

    path('users/add/', CreateUserView.as_view(), name='create_user')
]