# Generated by Django 4.2 on 2023-09-25 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_locations_delete_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='locations',
            new_name='location',
        ),
    ]