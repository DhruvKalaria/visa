# Generated by Django 3.2.6 on 2022-06-13 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0013_auto_20220611_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='acceptance_letter',
            field=models.BinaryField(null=True),
        ),
    ]
