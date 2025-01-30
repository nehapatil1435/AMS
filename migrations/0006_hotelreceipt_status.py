# Generated by Django 3.1.2 on 2024-11-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0005_remove_hotelreceipt_passengers'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelreceipt',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled')], default=1, max_length=45),
            preserve_default=False,
        ),
    ]
