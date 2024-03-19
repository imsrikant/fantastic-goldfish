from django.contrib import admin
from .models import User, Orphanage, Skill, UserSkill, Problem
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active")

@admin.register(Orphanage)
class OrphanageAdmin(admin.ModelAdmin):
    list_display = ("organization_name", "location", "contact_email")
    search_fields = ("organization_name", "location", "contact_email")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("skill_name", "skill_category")
    search_fields = ("skill_name", "skill_category")

@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = ("user", "skill")
    search_fields = ("user", "skill")

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("orphanage", "title", "status")
    search_fields = ("orphanage", "title", "status")
    list_filter = ("status",)


