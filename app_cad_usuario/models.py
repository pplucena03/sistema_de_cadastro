from django.db import models

# Create your models here.
class usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.TextField(max_length=50, null=False)
    date_of_birth = models.DateField(blank=True, null=True)