from django.shortcuts import render, redirect
from .models import User
# Create your views here.


def user_signup(request):
    signup_context = {"title": "Sign Up"}
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            signup_context["error"] = "Username already exists"
        elif User.objects.filter(email=email).exists():
            signup_context["error"] = "Email already exists"
        elif password == confirm_password:
            user = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            user.save()
            return redirect("user_login")
        else:
            signup_context["error"] = "Password and Confirm Password do not match"
    return render(request, "user/signup.html", signup_context)


def user_login(request):
    login_context = {"title": "Login"}
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Check if user exists and password is correct
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                # Redirect to home
                return redirect("/")
            else:
                login_context["error"] = "Incorrect password"
        except User.DoesNotExist:
            login_context["error"] = "Email does not exist"
    return render(request, "user/login.html", login_context)


def user_forgot_password(request):
    forgot_password_context = {"title": "Forgot Password"}
    return render(request, "user/forgot-password.html", forgot_password_context)
