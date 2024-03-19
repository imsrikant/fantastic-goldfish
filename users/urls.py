from django.urls import path
from ..user.views import user_signup, user_login, user_forgot_password

urlpatterns = [
    path("signup/", user_signup, name="user_signup"),
    path("login/", user_login, name="user_login"),
    path("forgot password/", user_forgot_password, name="user_forgot_password"),
]
