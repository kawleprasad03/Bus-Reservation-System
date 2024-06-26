# Generated by Django 4.2 on 2024-02-09 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_delete_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('bid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('busNumber', models.CharField(max_length=255)),
                ('busType', models.CharField(max_length=255)),
                ('departureTime', models.DateTimeField()),
                ('arrivalTime', models.DateTimeField()),
                ('totalTime', models.DurationField()),
                ('amount', models.IntegerField()),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.route')),
            ],
        ),
    ]
