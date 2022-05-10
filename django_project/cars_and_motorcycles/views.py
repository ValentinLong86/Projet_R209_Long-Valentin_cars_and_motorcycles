from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import motorcycleForm, carForm, marqueForm
from . import models


def index(request):
    return render(request, 'cars_and_motorcycles/index.html')


def cars(request):
    return render(request, 'cars_and_motorcycles/cars.html')


def motorcycles(request):
    return render(request, 'cars_and_motorcycles/motorcycles.html')


def add_object(request):
    if request.method == "POST":
        form = carForm(request)
        form2 = motorcycleForm(request)
        if form.is_valid():
            car = form.save()
            return render(request, "cars_and_motorcycles/index.html", {"car": car})  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        elif form2.is_valid():
            motorcycle = form2.save()
            return render(request, "cars_and_motorcycles/index.html", {"motorcycle": motorcycle})  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        else:
            return render(request, "cars_and_motorcycles/add_object.html", {"form": form, "form2": form2})
    else:
        form = carForm()
        form2 = motorcycleForm()
        return render(request, "cars_and_motorcycles/add_object.html", {"form": form, "form2": form2})


def traitement_add_object(request):
    pform = carForm(request.POST)
    pform2 = motorcycleForm(request.POST)
    if pform.is_valid():
        car = pform.save()
        return render(request, "cars_and_motorcycles/index.html", {"car": car})  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif pform2.is_valid():
        motorcycle = pform2.save()
        return render(request, "cars_and_motorcycles/index.html",
                      {"motorcycle": motorcycle})  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:
        return render(request, "cars_and_motorcycles/add_object.html", {"form": pform, "form2": pform2})


def listALLCars(request):
    liste = models.car.objects.all()
    return render(request, "cars_and_motorcycles/cars.html", {"liste": liste})


def listALLMotorcycles(request):
    liste = models.motorcycle.objects.all()
    return render(request, "cars_and_motorcycles/motorcycles.html", {"liste": liste})


def car_update(request, id):
    car = models.car.objects.get(pk=id)
    form = carForm(car.dico())
    return render(request, "cars_and_motorcycles/car_update.html", {"form": form, "id": id})


def traitement_car_update(request, id):
    lform = carForm(request.POST)
    if lform.is_valid():
        car = lform.save(commit=False)
        car.id = id
        car.save()
        return HttpResponseRedirect("/cars_and_motorcycles/cars/")
    else:
        return render(request, "cars_and_motorcycles/car_update.html", {"lform": lform, "id": id})


def motorcycle_update(request, id):
    motorcycle = models.motorcycle.objects.get(pk=id)
    form = motorcycleForm(motorcycle.dico())
    return render(request, "cars_and_motorcycles/motorcycle_update.html", {"form": form, "id": id})


def traitement_motorcycle_update(request, id):
    lform = motorcycleForm(request.POST)
    if lform.is_valid():
        motorcycle = lform.save(commit=False)
        motorcycle.id = id
        motorcycle.save()
        return HttpResponseRedirect("/cars_and_motorcycles/motorcycles/")
    else:
        return render(request, "cars_and_motorcycles/motorcycle_update.html", {"lform": lform, "id": id})


def delete_car(request, id):
    car = models.car.objects.get(pk=id)
    car.delete()
    return HttpResponseRedirect("/cars_and_motorcycles/cars/")


def delete_motorcycle(request, id):
    motorcycle = models.motorcycle.objects.get(pk=id)
    motorcycle.delete()
    return HttpResponseRedirect("/cars_and_motorcycles/motorcycles/")


def add_marque(request):
    liste = models.marque.objects.all()
    if request.method == "POST":
        form = marqueForm(request)
        if form.is_valid():
            marque = form.save()
            return render(request, "cars_and_motorcycles/index.html", {"marque": marque})  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        else:
            return render(request, "cars_and_motorcycles/marques.html", {"form": form, "liste": liste})
    else:
        form = marqueForm()
        return render(request, "cars_and_motorcycles/marques.html", {"form": form, "liste": liste})


def traitement_add_marque(request):
    pform = marqueForm(request.POST)
    if pform.is_valid():
        marque = pform.save()
        return render(request, "cars_and_motorcycles/index.html", {"marque": marque})  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:
        return render(request, "cars_and_motorcycles/marques.html", {"form": pform})


def delete_marque(request, id):
    pass


def update_marque(request, id):
    pass


def traitement_update_marque(request, id):
    pass
