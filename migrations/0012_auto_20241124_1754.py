# Generated by Django 3.1.2 on 2024-11-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0011_auto_20241124_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='iata_code',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='airline',
            name='icao_code',
            field=models.CharField(max_length=4),
        ),
    ]
