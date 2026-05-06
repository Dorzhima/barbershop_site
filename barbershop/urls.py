from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Services
    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/create/', views.service_create, name='service_create'),
    path('services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),
    
    # Masters
    path('masters/', views.master_list, name='master_list'),
    path('masters/<int:pk>/', views.master_detail, name='master_detail'),
    path('masters/create/', views.master_create, name='master_create'),
    path('masters/<int:pk>/edit/', views.master_edit, name='master_edit'),
    path('masters/<int:pk>/delete/', views.master_delete, name='master_delete'),
    
    # Bookings
    path('booking/', views.booking_create, name='booking_create'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:pk>/edit/', views.booking_edit, name='booking_edit'),
    path('bookings/<int:pk>/delete/', views.booking_delete, name='booking_delete'),
    
    # Reviews
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/create/', views.review_create, name='review_create'),
    path('reviews/<int:pk>/delete/', views.review_delete, name='review_delete'),
    path('reviews/<int:pk>/publish/', views.review_publish, name='review_publish'),
    
    # Contact
    path('contact/', views.contact_view, name='contact'),
]