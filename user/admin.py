# from django.contrib import admin
# from .models import User

# # Register your models here.


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ("username", "email", "user_type", "is_staff")
#     search_fields = ("username", "email")
#     list_filter = ("user_type", "is_staff")
#     ordering = ("username",)
#     filter_horizontal = ()
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#         ("Personal info", {"fields": ("first_name", "last_name", "email")}),
#         (
#             "Permissions",
#             {
#                 "fields": (
#                     "is_active",
#                     "is_staff",
#                     "is_superuser",
#                     "groups",
#                     "user_permissions",
#                 )
#             },
#         ),
#         ("Important dates", {"fields": ("last_login", "date_joined")}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("username", "email", "password1", "password2"),
#             },
#         ),
#     )
#     readonly_fields = ("last_login", "date_joined")
#     filter_horizontal = ("groups", "user_permissions")
#     list_per_page = 20
#     save_on_top = True
#     actions_on_top = True
#     actions_on_bottom = True
#     empty_value_display = "-empty-"
#     show_full_result_count = True
#     show_all = True
#     show_change_link = True
#     show_delete_link = True
#     show_save = True
#     show_save_as_new = True
