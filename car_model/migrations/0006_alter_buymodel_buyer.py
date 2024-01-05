# Generated by Django 4.2.7 on 2024-01-04 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car_model', '0005_buymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buymodel',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
