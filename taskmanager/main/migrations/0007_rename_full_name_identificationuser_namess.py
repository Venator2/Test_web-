# Generated by Django 4.0.1 on 2022-01-24 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_identificationuser_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identificationuser',
            old_name='full_name',
            new_name='namess',
        ),
    ]
