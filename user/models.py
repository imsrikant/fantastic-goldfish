from django.db import models
from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):
    user_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    contact_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    profile_picture = models.URLField(blank=True)

    def __str__(self):
        return self.email


class Orphanage(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # One user manages one orphanage
    organization_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    logo = models.URLField(blank=True)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()

    def __str__(self):
        return self.organization_name


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_category = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name
from django.db import models


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.skill.skill_name}"


class Problem(models.Model):
    orphanage = models.ForeignKey(Orphanage, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.orphanage.organization_name} - {self.title}"
