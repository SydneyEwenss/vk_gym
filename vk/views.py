from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ContactForm, AvailabilityForm
# from booking_functions.availability import check_availability
from django.http import HttpResponse

def home(request):
    context = {
        'css': 'home'
    }
    return render(request, 'vk/home.html', context)

def memberships(request):
    context = {
        'title': 'Memberships'
    }
    return render(request, 'vk/memberships.html', context)

def classes(request):
    context = {
        'title': 'Classes'
    }
    return render(request, 'vk/classes.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
            return redirect('home')
    else :
        form = ContactForm()
    context = {
        'title': 'Contact',
        'form': form
    }
    return render(request, 'vk/contact.html', context)

@login_required
def dashboard(request):
    context = {
        'bookings': Booking.objects.all()
    }
    return render(request, 'vk/dashboard.html', context)

@login_required
def booking(request):
    # if request.method == 'POST':
    #     form = AvailabilityForm(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         class_list = Class.objects.filter(classBooked=data['classBooking'])
    #         for classBooking in class_list:
    #             if check_availability(classBooking):
    #                 pass
    #         return redirect('home')
    # else :
    #     form = AvailabilityForm()
    context = {
        'classes': Class.objects.all()
    }
    return render(request, 'vk/booking.html', context)