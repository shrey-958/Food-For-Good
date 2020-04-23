from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField(null = True, blank = True)
    phone = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.user.username






