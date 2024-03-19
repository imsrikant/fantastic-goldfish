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



def terms(request):
    context = {
        "title": "Terms of Service",
    }
    return render(request, "terms.html", context)

def privacy(request):
    context = {
        "title": "Privacy Policy",
    }
    return render(request, "privacy.html", context)

def login(request):
    context = {
        "title": "Login",
    }
    return render(request, "login.html", context)

def signup(request):
    context = {
        "title": "Signup",
    }
    return render(request, "signup.html", context)
