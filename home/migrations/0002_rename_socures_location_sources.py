# Generated by Django 4.2 on 2023-09-21 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='socures',
            new_name='sources',
        ),
    ]
