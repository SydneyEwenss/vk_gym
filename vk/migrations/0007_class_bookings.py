# Generated by Django 5.0.1 on 2024-01-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vk', '0006_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='bookings',
            field=models.IntegerField(default=0),
        ),
    ]
