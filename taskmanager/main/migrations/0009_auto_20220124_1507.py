# Generated by Django 3.2 on 2022-01-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_identificationuser_namess'),
    ]

    operations = [
        migrations.AddField(
            model_name='identificationuser',
            name='full_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='identificationuser',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Прізвище'),
        ),
    ]
