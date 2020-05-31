from django.views.generic import TemplateView

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/login")

    return render(request, "registration/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("/login/")
        else:
            return redirect("/register/")
    return render(request, "registration/register.html")


def index_view(request):
    return render(request, "index.html")


def help_view(request):
    return render(request, "help.html")
