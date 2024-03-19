from django.shortcuts import render

# Create your views here.

def user_signup(request):
    signup_context = {"title": "Signup"}
    return render(request, "user/signup.html", signup_context)

def user_login(request):
    login_context = {"title": "Login"}
    return render(request, "user/login.html", login_context)
