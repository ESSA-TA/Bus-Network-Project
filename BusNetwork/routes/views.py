from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Station, Route
from .forms import CustomUserCreationForm


def index(request):
    routes = Route.objects.all()
    return render(request, "routes/index.html", {
        "routes": routes
    })


def route_detail(request, route_id):
    route = Route.objects.get(id=route_id)
    passengers = route.passengers.all()

    is_booked = False
    if request.user.is_authenticated:
        is_booked = route.passengers.filter(id=request.user.id).exists()

    return render(request, "routes/route_detail.html", {
        "route": route,
        "passengers": passengers,
        "is_booked": is_booked
    })


@login_required
def book(request, route_id):
    if request.method == "POST":
        route = Route.objects.get(id=route_id)
        action = request.POST.get("action")

        if action == "book":
            route.passengers.add(request.user)
        elif action == "unbook":
            route.passengers.remove(request.user)

        return HttpResponseRedirect(reverse('route_detail', args=(route.id,)))

 
    return HttpResponseRedirect(reverse('route_detail', args=(route_id,)))


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required  
def my_bookings(request):
    routes = Route.objects.filter(passengers=request.user)
    return render(request, 'routes/bookings.html', {'routes': routes})

def station_detail(request, station_id):
    station   = Station.objects.get(id=station_id)
    departing = Route.objects.filter(origin=station)
    arriving  = Route.objects.filter(destination=station)
    return render(request, 'routes/station_detail.html', {
        'station':   station,
        'departing': departing,
        'arriving':  arriving,
    })
