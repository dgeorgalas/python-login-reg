from django.shortcuts import render, redirect
from . models import Shows

def index(request):
    show_id = Shows.objects.all()
    context = {
        "show": show
    }
    return render(request, "first_app/index.html")

def show(request, show_id):
    context = {
        "show": Shows.objects.get(id=show_id)
    }
    return render(request, "first_app/show.html", context)

def all_shows(request):
    context = {
        "all_the_shows" : Shows.objects.all()
    }
    return render(request, "first_app/all_shows.html", context)

def edit(request, show_id):
    show = Shows.objects.get(id=show_id)
    context = {
        "show": show
    }
    return render(request, "first_app/edit.html", context)

def update(request, show_id):
    if request.method == "POST":
        show = Shows.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.description = request.POST['description']
        show.save()
        return redirect("/shows/" + str(show.id))




def create(request):
     if request.method == "POST":
        title = request.POST["title"]
        network = request.POST["network"]
        release_date = request.POST["release_date"]
        description = request.POST["description"]
        
        show = Shows.objects.create(title=title, network=network, release_date=release_date, description=description)
        return redirect( "/shows/" + str(show.id))

def delete(request, show_id):
    a = Shows.objects.get(id=show_id)
    a.delete()
    return redirect("/shows")
