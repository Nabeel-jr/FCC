# Generated by Django 5.1.1 on 2024-10-21 18:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0010_bikemodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
