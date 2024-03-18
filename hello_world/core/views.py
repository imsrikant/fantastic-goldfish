from django.shortcuts import render


def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)


def faq(request):
    context = {
        "title": "FAQ",
    }
    return render(request, "faq.html", context)


