# Generated by Django 3.2.6 on 2022-06-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0016_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='flight_reservation',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='work',
            name='flight_reservation',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]