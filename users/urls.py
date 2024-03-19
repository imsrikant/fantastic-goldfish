from django.urls import path
from users.views import user_signup

urlpatterns = [
    path("signup/", user_signup, name="user_signup"),
    # path("login/", user_login, name="user_login"),
    # path("forgot password/", user_forgot_password, name="user_forgot_password"),
]

