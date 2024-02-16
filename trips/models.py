from django.db import models

# Create your models here.
from django.db import models

budget_choices = [('f','food'),('l','lodging'),('t','transportation'),('e','entertainment'),('o','other')]

class Trip(models.Model):
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200,default='US')
    arrive_dt = models.DateTimeField("arrival date")
    depart_dt = models.DateTimeField("departure date")
    lodging = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.city
    


class Budget(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200, choices=budget_choices)
    cost = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.trip) + ' - ' + self.item
    
class Flight(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    airline = models.CharField(max_length=200)
    airports = models.CharField(max_length=200)
    arrive_time = models.DateTimeField("time of flight")
    depart_time = models.DateTimeField("time of return")
    notes = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.trip) + ' - ' + self.airline
    
class Attraction(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)
    item_type = models.CharField(max_length=200, choices=budget_choices, default=budget_choices[0])
    type = models.CharField(max_length=200)
    notes = models.CharField(max_length=200, blank=True, null=True)
    confirmed = models.BooleanField(default=False)
    cost = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.trip) + ' - ' + self.name