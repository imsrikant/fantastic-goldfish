from django.urls import path
from hello_world.core.views import index, faq

urlpatterns = [
    path("", index, name="index"),
    path("faq/", faq, name="faq"),
]


