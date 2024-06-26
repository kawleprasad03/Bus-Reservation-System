# Generated by Django 4.2 on 2024-01-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_locations_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('custid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=250)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
