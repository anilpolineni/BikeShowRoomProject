# Generated by Django 3.1.3 on 2021-01-11 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybooking',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='mybooking',
            name='tracking',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='awiting', max_length=50),
        ),
    ]
