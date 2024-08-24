from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# AbstractBaseUser
class usuarios(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True, null=False, default='')
    email = models.EmailField(max_length=100, unique=True, null=False, default='')
    password = models.TextField(max_length=50, null=False)
    date_of_birth = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
