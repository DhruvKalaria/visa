# Generated by Django 3.2.6 on 2022-06-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_auto_20220611_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='dath_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='dath_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='dath_of_birth',
            field=models.DateField(null=True),
        ),
    ]