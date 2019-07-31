from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def home(request):
    return render(request, 'first_app/home.html')


def register(request):
    errors = Users.object.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        name = request.POST["name"]
        alias = request.POST["alias"]
        email = request.POST["email"]
        password = request.POST["password"]
        date_of_birth = request.POST["date_of_birth"]
        user = Users.object.create(name=name, alias=alias, email=email, password=password, date_of_birth=date_of_birth)
        request.session["id"] = user.id
        return redirect("/quotes")

def login(request):
    errors = Users.object.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = Users.object.filter(email=request.POST["email"]) [0]
        # if(Users.object.filter(password=request.POST["password"]).exists()):
        request.session["id"] = user.id
        print(user.email)
        print(user.password)
        print(request.POST["password"])
        print(request.POST["password"] == user.password)
        print("==================")
        return redirect("/quotes")

def quotes(request):
    # differentiate which quotes the user has liked
    user = Users.object.get(id=request.session["id"])
    quotes = Quotes.object.all()
    non_favs = []
    for quote in quotes:
        if not quote.favorites.filter(id=request.session["id"]):
            non_favs.append(quote)
    # fav_quotes = user.favorites.all()
    # users = Users.object.all()
    # quote = Quotes.object.all() []
    # quotes = quote.favorites.all().exclude(id=request.session["id"])
    favorites = user.favorites.all()
    context = {
        "user" : user,
        # "users" : users,
        # "quotes" : quotes,
        "favorites" : favorites,
        "non_favs" : non_favs
    }
    return render(request, 'first_app/quotes.html', context)


def contribute(request):
    errors = Quotes.object.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/quotes")
    else:
        user = Users.object.get(id=request.session["id"])
        quoted_by = request.POST["quoted_by"]
        message = request.POST["message"]
        Quotes.object.create(quoted_by=quoted_by, message=message, user=user)
        return redirect("/quotes")

def add_to_favorites(request, non_fav_id):
    quote = Quotes.object.get(id=non_fav_id)
    user = Users.object.get(id=request.session["id"])
    favorite = user.favorites.add(quote)
    print(user.favorites.all())
    print("==================")
    return redirect("/quotes")

def remove(request, favorite_id):
    user = Users.object.get(id=request.session["id"])
    favorite = user.favorites.remove(favorite_id)
    return redirect("/quotes")

def users(request, quote_user_id):
    user = Users.object.get(id=quote_user_id)
    user_quotes = Quotes.object.filter(user=user)
    count = user_quotes.count
    context = {
        "user" : user,
        "user_quotes" : user_quotes,
        "count" : count
    }
    return render(request, 'first_app/users.html', context)

def logout(request):
    del request.session["id"]
    return redirect("/")
