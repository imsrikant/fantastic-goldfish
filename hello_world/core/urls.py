from django.urls import path
from hello_world.core.views import index, faq, about, contact

urlpatterns = [
    path("", index, name="index"),
    path("faq/", faq, name="faq"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
]
