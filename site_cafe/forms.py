from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user_name', 'user_phone', 'user_datetime', 'user_count', 'special_requests']
        labels = {
            'user_name': 'Enter your name',
            'user_phone': 'Enter your phone number',
            'user_datetime': 'Enter date and time',
            'user_count': 'Number of guests',
            'special_requests': 'Special requests',
        }
        widgets = {
            'user_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }