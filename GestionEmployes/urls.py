from django.urls import path
from .views import EmployeeDetailView, EmployeeListCreateView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employees-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employees-details'),
]