from django.forms import ModelForm, widgets
from django import forms
from .models import Trip, Budget, Flight, Attraction

budget_choices = [('f','food'),('l','lodging'),('t','transportation'),('e','entertainment'),('o','other')]

# Create the form class.
class FlightForm(ModelForm):
    class Meta:
        model = Flight
        trip = forms.ModelChoiceField(queryset=Trip.objects.all())
        fields = '__all__'
        widgets = {
            'arrive_time': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'depart_time': widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        
class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'
        widgets = {
            'arrive_dt': widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'depart_dt': widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        
class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        trip = forms.ModelChoiceField(queryset=Trip.objects.all())
        item_type = forms.ChoiceField(choices=budget_choices)
        fields = '__all__'
        
class AttractionForm(ModelForm):
    class Meta:
        model = Attraction
        trip = forms.ModelChoiceField(queryset=Trip.objects.all())
        item_type = forms.ChoiceField(choices=budget_choices)
        fields = '__all__'
        