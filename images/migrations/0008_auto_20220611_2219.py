# Generated by Django 3.2.6 on 2022-06-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_auto_20220611_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('progress', 'In Progress'), ('rejected', 'Rejected')], default='new', max_length=32),
        ),
        migrations.AddField(
            model_name='tour',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('progress', 'In Progress'), ('rejected', 'Rejected')], default='new', max_length=32),
        ),
        migrations.AddField(
            model_name='work',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('progress', 'In Progress'), ('rejected', 'Rejected')], default='new', max_length=32),
        ),
    ]