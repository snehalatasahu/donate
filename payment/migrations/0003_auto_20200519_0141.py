# Generated by Django 3.0.4 on 2020-05-18 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20200519_0132'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Donors',
            new_name='Donor',
        ),
    ]
