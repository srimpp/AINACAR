from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='users'