from django.db import models

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.service_name