from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import motorcycleForm, carForm, carMarqueForm
from . import models


def index(request):
    return render(request, 'cars_and_motorcycles/index.html/')


def list_all_cars(request):
    car_list = models.car.objects.all()
    return render(request, "cars_and_motorcycles/cars_list.html/", {"liste": car_list})


def car_update(request, id):
    car = models.car.objects.get(pk=id)
    form = carForm(car.dico())
    return render(request, "cars_and_motorcycles/car_update.html/", {"form": form, "id": id})


def t_car_update(request, id):
    t_form = carForm(request.POST)
    if t_form.is_valid():
        car = t_form.save(commit=False)
        car.id = id
        car.save()
        return HttpResponseRedirect("/cars_and_motorcycles/cars_list/")
    else:
        return render(request, "cars_and_motorcycles/car_update.html/", {"form": t_form, "id": id})


def delete_car(request, id):
    car = models.car.objects.get(pk=id)
    car.delete()
    return HttpResponseRedirect("/cars_and_motorcycles/cars_list/")


def list_all_motorcycles(request):
    m_list = models.motorcycle.objects.all()
    return render(request, "cars_and_motorcycles/motorcycles_list.html/", {"liste": m_list})


def motorcycle_update(request, id):
    motorcycle = models.motorcycle.objects.get(pk=id)
    form = motorcycleForm(motorcycle.dico())
    return render(request, "cars_and_motorcycles/motorcycle_update.html/", {"form": form, "id": id})


def t_motorcycle_update(request, id):
    t_form = motorcycleForm(request.POST)
    if t_form.is_valid():
        motorcycle = t_form.save(commit=False)
        motorcycle.id = id
        motorcycle.save()
        return HttpResponseRedirect("/cars_and_motorcycles/motorcycles_list/")
    else:
        return render(request, "cars_and_motorcycles/motorcycle_update.html/", {"form": t_form, "id": id})


def delete_motorcycle(request, id):
    motorcycle = models.motorcycle.objects.get(pk=id)
    motorcycle.delete()
    return HttpResponseRedirect("/cars_and_motorcycles/motorcycles_list/")


def add_object(request):
    if request.method == "POST":
        form = carForm(request)
        form2 = motorcycleForm(request)
        if form.is_valid():
            car = form.save()
            return HttpResponseRedirect("/cars_and_motorcycles/cars_list/")
        elif form2.is_valid():
            motorcycle = form2.save()
            return HttpResponseRedirect("/cars_and_motorcycles/motorcycles_list/")
        else:
            return render(request, "cars_and_motorcycles/add_object.html/", {"form": form, "form2": form2})
    else:
        form = carForm()
        form2 = motorcycleForm()
        return render(request, "cars_and_motorcycles/add_object.html/", {"form": form, "form2": form2})


def t_add_object(request):
    t_form = carForm(request.POST)
    t_form2 = motorcycleForm(request.POST)
    if t_form.is_valid():
        car = t_form.save()
        return HttpResponseRedirect("/cars_and_motorcycles/cars_list/")
    elif t_form2.is_valid():
        motorcycle = t_form2.save()
        return HttpResponseRedirect("/cars_and_motorcycles/motorcycles_list/")
    else:
        return render(request, "cars_and_motorcycles/add_object.html/", {"form": t_form, "form2": t_form2})


def add_marque(request):
    car_list = models.car_marque.objects.all()
    if request.method == "POST":
        form = carMarqueForm(request)
        if form.is_valid():
            marque = form.save()
            return render(request, "cars_and_motorcycles/index.html/")
        else:
            return render(request, "cars_and_motorcycles/marques.html/", {"form": form, "liste": car_list})
    else:
        form = carMarqueForm()
        return render(request, "cars_and_motorcycles/marques.html/", {"form": form, "liste": car_list})


def t_add_car_marque(request):
    t_form = carMarqueForm(request.POST)
    if t_form.is_valid():
        car_marque = t_form.save()
        return HttpResponseRedirect("/cars_and_motorcycles/add_marque/")
    else:
        return render(request, "cars_and_motorcycles/marques.html/", {"form": t_form})


def delete_car_marque(request, id):
    car_marque = models.car_marque.objects.get(pk=id)
    car_marque.delete()
    return HttpResponseRedirect("/cars_and_motorcycles/add_marque/")


def update_car_marque(request, id):
    car_marque = models.car_marque.objects.get(pk=id)
    form = carMarqueForm(car_marque.dico())
    return render(request, "cars_and_motorcycles/update_car_marque.html/", {"form": form, "id": id})


def t_update_car_marque(request, id):
    t_form = carMarqueForm(request.POST)
    if t_form.is_valid():
        car_marque = t_form.save(commit=False)
        car_marque.id = id
        car_marque.save()
        return HttpResponseRedirect("/cars_and_motorcycles/add_marque/")
    else:
        return render(request, "cars_and_motorcycles/marque_update.html/", {"form": t_form, "id": id})
