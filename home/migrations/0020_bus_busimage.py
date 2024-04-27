# Generated by Django 4.2 on 2024-02-27 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_busimage_bid_delete_bus_delete_busimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('bid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('busNumber', models.CharField(max_length=255)),
                ('busType', models.CharField(max_length=255)),
                ('departureTime', models.CharField(max_length=50)),
                ('arrivalTime', models.CharField(max_length=50)),
                ('totalTime', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('rid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.route')),
            ],
        ),
        migrations.CreateModel(
            name='busImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.BinaryField()),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.bus')),
            ],
        ),
    ]
