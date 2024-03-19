from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email']
    search_fields = ['first_name', 'last_name', 'username', 'email']
    list_filter = ['first_name', 'last_name', 'username', 'email']
    list_per_page = 10
    list_max_show_all = 100
    list_select_related = False
    list_display_links = ['first_name', 'last_name', 'username', 'email']
    list_editable = []
