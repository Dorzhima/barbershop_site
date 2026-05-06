from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Service, Master, Booking, Review, Contact
from .forms import ServiceForm, MasterForm, BookingForm, BookingEditForm, ReviewForm

# ========== HOME PAGE ==========
def home(request):
    services = Service.objects.all()[:6]
    masters = Master.objects.all()[:4]
    reviews = Review.objects.filter(is_published=True)[:3]
    contact = Contact.objects.first()
    return render(request, 'barbershop/home.html', {
        'services': services,
        'masters': masters,
        'reviews': reviews,
        'contact': contact,
    })

# ========== SERVICE CRUD ==========
def service_list(request):
    services = Service.objects.all()
    return render(request, 'barbershop/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'barbershop/service_detail.html', {'service': service})

@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service created successfully!')
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'barbershop/service_form.html', {'form': form, 'title': 'Add Service'})

@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully!')
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'barbershop/service_form.html', {'form': form, 'title': 'Edit Service'})

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    messages.success(request, 'Service deleted successfully!')
    return redirect('service_list')

# ========== MASTER CRUD ==========
def master_list(request):
    masters = Master.objects.all()
    return render(request, 'barbershop/master_list.html', {'masters': masters})

def master_detail(request, pk):
    master = get_object_or_404(Master, pk=pk)
    return render(request, 'barbershop/master_detail.html', {'master': master})

@login_required
def master_create(request):
    if request.method == 'POST':
        form = MasterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Master added successfully!')
            return redirect('master_list')
    else:
        form = MasterForm()
    return render(request, 'barbershop/master_form.html', {'form': form, 'title': 'Add Master'})

@login_required
def master_edit(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.method == 'POST':
        form = MasterForm(request.POST, request.FILES, instance=master)
        if form.is_valid():
            form.save()
            messages.success(request, 'Master updated successfully!')
            return redirect('master_list')
    else:
        form = MasterForm(instance=master)
    return render(request, 'barbershop/master_form.html', {'form': form, 'title': 'Edit Master'})

@login_required
def master_delete(request, pk):
    master = get_object_or_404(Master, pk=pk)
    master.delete()
    messages.success(request, 'Master deleted successfully!')
    return redirect('master_list')

# ========== BOOKING ==========
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.status = 'pending'
            booking.save()
            messages.success(request, 'Your booking has been created! We will contact you soon.')
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'barbershop/booking_form.html', {'form': form})

@login_required
def booking_list(request):
    bookings = Booking.objects.all().order_by('-date', '-time')
    return render(request, 'barbershop/booking_list.html', {'bookings': bookings})

@login_required
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingEditForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('booking_list')
    else:
        form = BookingEditForm(instance=booking)
    return render(request, 'barbershop/booking_edit.html', {'form': form, 'booking': booking})

@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    messages.success(request, 'Booking deleted successfully!')
    return redirect('booking_list')

# ========== REVIEW ==========
def review_list(request):
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'barbershop/review_list.html', {'reviews': reviews})

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.is_published = False  # нужно одобрение админа
            review.save()
            messages.success(request, 'Thank you for your review! It will appear after moderation.')
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'barbershop/review_form.html', {'form': form})

@login_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    messages.success(request, 'Review deleted successfully!')
    return redirect('review_list')

@login_required
def review_publish(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.is_published = True
    review.save()
    messages.success(request, 'Review published!')
    return redirect('review_list')

# ========== CONTACT ==========
def contact_view(request):
    contact = Contact.objects.first()
    return render(request, 'barbershop/contact.html', {'contact': contact})