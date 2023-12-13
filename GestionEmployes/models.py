from django.db import models
from django.conf import settings
from GestionServices.models import Service

class Employee(models.Model):
    department = models.CharField(max_length=50)
    assigned_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=191)
    employee_contact = models.CharField(max_length=30)
    adress = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.employee_id
