# Generated by Django 3.1.2 on 2024-11-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0007_auto_20241124_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelreceipt',
            name='num_rooms',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotelreceipt',
            name='total_cost',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
