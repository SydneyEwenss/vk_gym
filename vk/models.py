from django.db import models
from datetime import datetime
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Class(models.Model):
    CLASSES = (
        ('YOGA', 'YOGA'),
        ('SPIN', 'SPINNING'),
        ('FFT', 'FUNCTIONAL FITNESS TRAINING')
    )

    TIMES = (
        ('10', '10 AM'),
        ('11', '11 AM'),
        ('12', '12 PM'),
        ('13', '1 PM'),
        ('14', '2 PM'),
        ('15', '3 PM'),
        ('16', '4 PM'),
    )

    classBooked = models.CharField(max_length=4, choices=CLASSES)
    day = models.DateField()
    time = models.CharField(max_length=2, choices=TIMES)
    timeBooked = models.DateTimeField(default=datetime.now)
    capacity = models.IntegerField(default=20)
    bookings = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = "Classes"

    def __str__(self):
        return f'{self.classBooked} on {self.day} at {self.time} with capacity: {self.bookings}/{self.capacity}'
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classBooked = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} booked {self.classBooked}"
    

