from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Service, Master, Booking, Review, Contact

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    search_fields = ('name',)

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'phone')
    search_fields = ('full_name', 'specialization')
    filter_horizontal = ('services',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_phone', 'date', 'time', 'status', 'master')
    list_filter = ('status', 'date', 'master')
    search_fields = ('client_name', 'client_phone')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'is_published', 'created_at')
    list_filter = ('is_published', 'rating')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')