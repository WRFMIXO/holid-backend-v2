from django.db import models
from django.conf import settings
from GestionUtilisateurs.models import CustomUser
from GestionServices.models import Service

# Create your models here.
class Permission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='custom_user_permissions')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    can_read = models.BooleanField(default=False)
    can_write = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'service']

    def __str__(self):
        return f"{self.user.email} - {self.service.service_name}"