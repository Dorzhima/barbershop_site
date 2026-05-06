from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Master(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='masters/', blank=True, null=True)
    phone = models.CharField(max_length=20)
    bio = models.TextField(blank=True)
    services = models.ManyToManyField(Service, related_name='masters')

    def __str__(self):
        return self.full_name

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    master = models.ForeignKey(Master, on_delete=models.PROTECT, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='bookings')

    def __str__(self):
        return f"{self.client_name} - {self.date} {self.time}"

class Review(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    booking = models.OneToOneField(Booking, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.author} - {self.rating}★"

class Contact(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    work_hours = models.CharField(max_length=100)

    def __str__(self):
        return "Contact Information"