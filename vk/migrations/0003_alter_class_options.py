# Generated by Django 5.0.1 on 2024-01-20 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vk', '0002_rename_classes_class'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
    ]
