from django import forms
from .models import Service, Master, Booking, Review

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'price', 'duration', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['full_name', 'specialization', 'photo', 'phone', 'bio', 'services']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'services': forms.CheckboxSelectMultiple(),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['client_name', 'client_phone', 'date', 'time', 'master', 'service']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class BookingEditForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['client_name', 'client_phone', 'date', 'time', 'status', 'master', 'service']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }