from django.db import models

# Create your models here.
class HotelInformations(models.Model):
    hotel_name = models.CharField(max_length=255, unique=True, primary_key=True)
    hotel_city = models.CharField(max_length=255)
    hotel_country = models.CharField(max_length=255)
    hotel_total_employee = models.PositiveIntegerField()
    hotel_creation_date = models.DateField()
    hotel_total_rooms_number = models.PositiveIntegerField
