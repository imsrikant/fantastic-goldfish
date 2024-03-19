from django.urls import path
from hello_world.core.views import index, faq, about, contact, terms, privacy, login, signup

urlpatterns = [
    path("", index, name="index"),
    path("faq/", faq, name="faq"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("terms/", terms, name="terms"),
    path("privacy/", privacy, name="privacy"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
]
