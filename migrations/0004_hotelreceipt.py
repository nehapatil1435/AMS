# Generated by Django 3.1.2 on 2024-11-24 03:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_hotelbooking_num_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_no', models.CharField(max_length=6, unique=True)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('room_type', models.CharField(choices=[('AC', 'AC'), ('Non-AC', 'Non-AC')], max_length=10)),
                ('num_rooms', models.PositiveIntegerField()),
                ('total_cost', models.FloatField()),
                ('booking_date', models.DateTimeField(default=datetime.datetime.now)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=45)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipts', to='flight.hotel')),
                ('passengers', models.ManyToManyField(blank=True, related_name='hotel_receipts', to='flight.Passenger')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_receipts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
