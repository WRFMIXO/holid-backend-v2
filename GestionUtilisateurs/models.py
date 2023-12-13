from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from GestionServices.models import Service
from GestionEmployes.models import Employee


# UserManager Class Model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    
# User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    services = models.ManyToManyField(Service, through='GestionPermissions.Permission')
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        # Ajoutez ces lignes pour spécifier des noms de relations inverses personnalisés
        # pour éviter les conflits avec les modèles intégrés Group et Permission
        app_label = 'GestionUtilisateurs'
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.email