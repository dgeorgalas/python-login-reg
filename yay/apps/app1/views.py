from django.shortcuts import render, HttpResponse

def index(request) :
    return HttpResponse("this is the equivalent of eggs")

def bears(request) :
    return HttpResponse("this is the equivalent of big scary bears")

def abe(request) :
    return HttpResponse("this is the equivalent of abe")
