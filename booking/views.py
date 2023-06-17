from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaulttags import regroup

from .models import  *
# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()[:3]
    return render(request, 'booking/index.html', {'restaurants': restaurants})

def restaurants_list(request):
    restaurants = Restaurant.objects.all()

    return render(request, 'main/restaurants.html', {'restaurants': restaurants})



def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, id=pk)
    menus = restaurant.menus.all()

    return render(request, 'main/single_restaurant.html', {'restaurant': restaurant, 'menus': menus})


def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')


def restaurant_booking(request, pk):
    restaurant = get_object_or_404(Restaurant, id=pk)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        party_size = request.POST['party_size']

        reservation = Reservation(restaurant=restaurant, name=name, email=email, date=date, time=time, party_size=party_size)
        reservation.save()

        return redirect('confirmation')

    context = {'restaurant': restaurant}
    return render(request, 'main/booking.html', context)

def confirmation(request):
    return render(request, 'main/confirmation.html')


def booking_confirmation(request):
    # Retrieve the latest reservation made by the user
    latest_reservation = Reservation.objects.latest('id')

    # Send the booking confirmation email
    send_booking_confirmation_email(latest_reservation)

    return render(request, 'main/booking_confirmation.html', {'reservation': latest_reservation})

def send_booking_confirmation_email(reservation):
    subject = 'Booking Confirmation - RestoReserve'
    message = f'Thank you for your reservation at {reservation.restaurant.name}!'
    message += f'\n\nReservation Details:'
    message += f'\nRestaurant: {reservation.restaurant.name}'
    message += f'\nDate: {reservation.date}'
    message += f'\nTime: {reservation.time}'
    message += f'\nParty Size: {reservation.party_size}'
    message += '\n\nWe look forward to serving you. Enjoy your meal!'
    from_email = 'noreply@restoreserve.com'
    recipient_email = reservation.email

    send_mail(subject, message, from_email, [recipient_email])



