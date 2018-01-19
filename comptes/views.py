# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, UserLogoutForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.http.response import HttpResponse


def user_signin(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(username=email, password=password)
        login(request, user)
        if request.user.is_authenticated():
            return redirect("/")
    return render(request, 'comptes/connexion.html', {"form": form})


def user_signup(request):
    reg = False
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():

        u = request.POST["username"]
        e = request.POST["email"]
        p = request.POST["password"]
        print(u)
        print(p)
        user = User(username=u,email=e)
        user.set_password(p)
        user.save()
        reg = True
        return redirect("/compte/connexion")

    return render(request, 'comptes/inscription.html', {"form": form, "reg": reg})


def user_logout(request):
    form = UserLogoutForm(request.POST or None)
    logout(request)
    return render(request, 'comptes/connexion.html', locals())


def user_validation(request):
    return HttpResponse("user_validation")


def user_profile(request):


    return HttpResponse("user_validation")


def user_update(request, id_user):
    if int(id_user) != 7:
        raise Http404
    return HttpResponse("user_update")


def success(request):
    return render(request, "ads/index.html")
