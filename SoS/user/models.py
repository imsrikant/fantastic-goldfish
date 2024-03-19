from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ("orphanage", "Orphanage"),
        ("volunteer", "Volunteer"),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
