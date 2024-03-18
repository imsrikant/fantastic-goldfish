from django.shortcuts import render


def index(request):
    context = {
        "title": "Skills For Smile",
    }
    return render(request, "index.html", context)


def faq(request):
    context = {
        "title": "FAQ",
    }
    return render(request, "faq.html", context)


def about(request):
    context = {
        "title": "About",
    }
    return render(request, "about.html", context)


def contact(request):
    context = {
        "title": "Contact",
    }
    return render(request, "contact.html", context)

