from vk.models import *

def check_availability(classBooked):
    booking = Booking.objects.filter(classBooked=classBooked)
    if booking.classBooked.bookings < booking.classBooked.capacity:
        return True
    return False