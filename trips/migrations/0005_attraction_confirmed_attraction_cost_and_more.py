# Generated by Django 4.2.10 on 2024-02-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trips", "0004_flight_attraction"),
    ]

    operations = [
        migrations.AddField(
            model_name="attraction",
            name="confirmed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="attraction",
            name="cost",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="attraction",
            name="address",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="attraction",
            name="notes",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="flight",
            name="notes",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="trip",
            name="notes",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]