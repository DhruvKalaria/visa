# Generated by Django 3.2.6 on 2022-06-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0017_auto_20220615_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='contract',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
