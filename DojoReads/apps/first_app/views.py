from django.shortcuts import render, HttpResponse

def login(request) :
    return HttpResponse("this is the login route")

def books(request) :
    return HttpResponse("this is the books route")

def add_book(request) :
    return HttpResponse("this is the add_book route")


# Create your views here.
