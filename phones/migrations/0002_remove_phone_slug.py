# Generated by Django 3.1.2 on 2024-08-04 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='slug',
        ),
    ]
