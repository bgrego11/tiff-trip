from django.contrib import admin

from .models import Trip, Budget, Flight, Attraction 

admin.site.register(Trip)
admin.site.register(Budget)
admin.site.register(Flight)
admin.site.register(Attraction)
