from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    print("======================")

    return render(request, 'first_app/index.html')

def register(request):
    errors = Users.object.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        Users.object.create(first_name=first_name, last_name=last_name, email=email, password=password)
        request.session['first_name'] = request.POST["first_name"]
        return redirect("/success")

def success(request):
    last_user = Users.object.last()
    context = {
        "last_user" : last_user
        }
    return render(request, 'first_app/success.html', context)


def log_out(request):
    del request.session["first_name"]
    return redirect("/")


def login(request):
    if(Users.object.filter(email=request.POST["email"]).exists()):
        user = Users.object.filter(email=request.POST["email"]) [0]
        if(Users.object.filter(password=request.POST["password"]).exists()):
            request.session["first_name"] = user.first_name
            return redirect("/success")
    return redirect("/")