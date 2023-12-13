from django.urls import path
from .views import CreateServiceView, ListServiceViewDetailled, DeleteServiceView, RetrieveUpdateServiceView, ListServicesView

urlpatterns = [
    path('services/create/', CreateServiceView.as_view(), name='services-list-create'),
    path('services-with-details/', ListServiceViewDetailled.as_view(), name='list-services-with-details'),
    path('services/<int:pk>/', RetrieveUpdateServiceView.as_view(), name='update-service'),
    path('services/<int:pk>/delete/', DeleteServiceView.as_view(), name='delete-service'),
    path('services/', ListServicesView.as_view(), name='services-list'),
]