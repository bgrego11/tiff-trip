from django.shortcuts import render, redirect
from django.template import loader


# Create your views here.
from django.http import Http404
from .models import Trip, Budget, Flight, Attraction
from .forms import FlightForm, BudgetForm, AttractionForm, TripForm


def trip_add(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            trip = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('detail', trip.id)

    else:
        form = TripForm()

    return render(request,
                'trips/trip_add.html',
                {'form': form})

def index(request):
    latest_trip_list = Trip.objects.order_by("-arrive_dt")[:5]
    context = {
        "latest_trip_list": latest_trip_list,
    }
    return render(request, "trips/index.html", context)

def detail(request, trip_id):
    try:
        trip = Trip.objects.get(pk=trip_id)
        try:
            budgets = Budget.objects.filter(trip__pk=trip_id)
        except:
            budgets = None
        try:
            flights = Flight.objects.filter(trip__pk=trip_id)
        except:
            flights = None
        try:
            attractions = Attraction.objects.filter(trip__pk=trip_id)
        except:
            attractions = None
    except:
        raise Http404("trip not found")
    context = {
        "trip": trip,
        "budgets": budgets,
        "flights": flights,
        "attractions": attractions
    }
    return render(request, "trips/detail.html",context)


def flight_add(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            flight = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('detail', flight.trip_id)

    else:
        form = FlightForm()

    return render(request,
                'trips/flight_add.html',
                {'form': form})


def flight_update(request, id):
    flight = Flight.objects.get(id=id)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
        # update the existing `Band` in the database
            form.save()
        # redirect to the detail page of the `Band` we just updated
            return redirect('detail', flight.trip_id)
    else:
            form = FlightForm(instance=flight) # prepopulate the form with an existing band
    return render(request,
                    'trips/flight_update_form.html',
                    {'form': form})
    
def budget_add(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            budget = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('detail', budget.trip_id)

    else:
        form = BudgetForm()

    return render(request,
                'trips/budget_add.html',
                {'form': form})
    
def budget_update(request, id):
    budget = Budget.objects.get(id=id)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
        # update the existing `Band` in the database
            form.save()
        # redirect to the detail page of the `Band` we just updated
            return redirect('detail', budget.trip_id)
    else:
            form = BudgetForm(instance=budget) # prepopulate the form with an existing band
    return render(request,
                    'trips/budget_update_form.html',
                    {'form': form})

def attraction_add(request):
    if request.method == 'POST':
        form = AttractionForm(request.POST)
        if form.is_valid():
            # create a new `Band` and save it to the db
            attraction = form.save()
            # redirect to the detail page of the band we just created
            # we can provide the url pattern arguments as arguments to redirect function
            return redirect('detail', attraction.trip_id)

    else:
        form = AttractionForm()

    return render(request,
                'trips/attraction_add.html',
                {'form': form})
    
def attraction_update(request, id):
    attraction = Attraction.objects.get(id=id)
    if request.method == 'POST':
        form = AttractionForm(request.POST, instance=attraction)
        if form.is_valid():
        # update the existing `Band` in the database
            form.save()
        # redirect to the detail page of the `Band` we just updated
            return redirect('detail', attraction.trip_id)
    else:
            form = AttractionForm(instance=attraction) # prepopulate the form with an existing band
    return render(request,
                    'trips/budget_add.html',
                    {'form': form})