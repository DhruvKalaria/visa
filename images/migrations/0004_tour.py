# Generated by Django 3.2.6 on 2022-05-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20220523_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_status', models.FileField(null=True, upload_to='')),
                ('economic_activity', models.FileField(null=True, upload_to='')),
                ('acceptance_letter', models.FileField(null=True, upload_to='')),
                ('passport', models.FileField(null=True, upload_to='')),
                ('deed_for_company', models.FileField(null=True, upload_to='')),
                ('embassy_fee_reciept', models.FileField(null=True, upload_to='')),
                ('insurance', models.FileField(null=True, upload_to='')),
                ('bank_statement', models.FileField(null=True, upload_to='')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('name', models.CharField(max_length=50, null=True)),
                ('e_mail', models.CharField(max_length=100, null=True)),
                ('dath_of_birth', models.CharField(max_length=50, null=True)),
                ('sponser', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('passport_number', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
