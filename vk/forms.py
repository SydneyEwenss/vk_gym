from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class AvailabilityForm(forms.Form):
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

    classBooking = forms.ChoiceField(choices=CLASSES, required=True)
    time = forms.ChoiceField(choices=TIMES, required=True)
    day = forms.DateField(required=True)