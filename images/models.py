from django.db import models


# Create your models here.

class File(models.Model):
    degree = models.FileField(blank=False, null=True)
    transcript = models.FileField(blank=False, null=True)
    acceptance_letter = models.FileField(blank=False, null=True)
    passport = models.FileField(blank=False, null=True)
    university_fee_reciept = models.FileField(blank=False, null=True)
    embassy_fee_reciept = models.FileField(blank=False, null=True)
    insurance = models.FileField(blank=False, null=True)
    bank_statement = models.FileField(blank=False, null=True)
    image = models.ImageField(blank=False, null=True)
    #   file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50, null=True)
    e_mail = models.CharField(max_length=100, null=True)
    dath_of_birth = models.CharField(max_length=50, null=True)
    sponser = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    passport_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tour(models.Model):
    cover_letter = models.FileField(blank=False, null=True)
    proof_of_accomodation = models.FileField(blank=False, null=True)
    passport = models.FileField(blank=False, null=True)
    flight_reservation = models.FileField(blank=False, null=True)
    embassy_fee_reciept = models.FileField(blank=False, null=True)
    insurance = models.FileField(blank=False, null=True)
    bank_statement = models.FileField(blank=False, null=True)
    image = models.ImageField(blank=False, null=True)
    #   file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50, null=True)
    e_mail = models.CharField(max_length=100, null=True)
    dath_of_birth = models.CharField(max_length=50, null=True)
    sponser = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    passport_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Work(models.Model):
    legal_status = models.FileField(blank=False, null=True)
    economic_activity = models.FileField(blank=False, null=True)
    passport = models.FileField(blank=False, null=True)
    deed_for_company = models.FileField(blank=False, null=True)
    embassy_fee_reciept = models.FileField(blank=False, null=True)
    insurance = models.FileField(blank=False, null=True)
    bank_statement = models.FileField(blank=False, null=True)
    image = models.ImageField(blank=False, null=True)
    #   file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50, null=True)
    e_mail = models.CharField(max_length=100, null=True)
    dath_of_birth = models.CharField(max_length=50, null=True)
    sponser = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    passport_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
