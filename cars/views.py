from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.contrib import messages


def some_view(request):
    form = SomeForm()
    if request.method == "POST":
        form = SomeForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    context = {
        "form":form
    }
    return render(request, 'car_detail.html', context)


def car_list(request):
	context = {
		"cars": Car.objects.all()
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	context = {
		"car" : Car.objects.get(id=car_id)
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Created!")
            return redirect('car-list')
        print(form.errors)
    context = {
        "form": form
    }
    return render(request, 'car_create.html', context)


def car_update(request, car_id):
    car = Car.objects.get(id=car_id)
    form = CarForm(instance=car)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES or None, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car-list')
        print (form.errors)
    context = {
    "form": form,
    "car": car,
    }
    return render(request, 'update_car.html', context)


def car_delete(request, car_id):
  Car.objects.get(id=car_id).delete()
  messages.success(request, "Successfully Deleted!")
  return redirect('car-list')

