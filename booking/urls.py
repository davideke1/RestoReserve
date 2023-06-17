from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='homepage'),
    path('restaurants/', views.restaurants_list, name='restaurant_list'),
    path('restaurant/<int:pk>', views.restaurant_detail, name='restaurant_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('booking/<int:pk>/',views.restaurant_booking, name='booking'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation')
]