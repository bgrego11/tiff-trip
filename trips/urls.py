from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:trip_id>/", views.detail, name="detail"),
    path("flights/<int:id>/change/", views.flight_update, name="flight_update"),
    path("budgets/<int:id>/change/", views.budget_update, name="budget_update"),
    path("attractions/<int:id>/change/", views.attraction_update, name="attraction_update"),
    path("flights/add/", views.flight_add, name="flight_add"),
    path("budgets/add/", views.budget_add, name="budget_add"),
    path("attractions/add/", views.attraction_add, name="attraction_add"),
    path("add/", views.trip_add, name="trip_add"),
]