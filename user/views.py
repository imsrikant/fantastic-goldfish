from django.shortcuts import render

# Create your views here.


def user_signup(request):
    signup_context = {"title": "Sign Up"}
    return render(request, "user/signup.html", signup_context)


def user_login(request):
    login_context = {"title": "Login"}
    return render(request, "user/login.html", login_context)


def user_forgot_password(request):
    forgot_password_context = {"title": "Forgot Password"}
    return render(request, "user/forgot-password.html", forgot_password_context)
