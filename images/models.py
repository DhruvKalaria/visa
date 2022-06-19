from django.db import models

# Create your models here.
STATUS = (
    ('new', "New"),
    ("in-progress", "In Progress"),
    ("rejected", "Rejected"),
    ("approved", "Approved"),
)

STATUS1 = (
    ('new', "New"),
    ("in-progress", "In Progress"),
    ("rejected", "Rejected"),
    ("solved", "Solved"),
)


class File(models.Model):
    id = models.AutoField(primary_key=True)
    #   file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50, null=True)
    e_mail = models.CharField(max_length=100, null=True)
    dath_of_birth = models.CharField(max_length=50, null=True)
    sponser = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    passport_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    image = models.ImageField(blank=False, null=True)
    degree = models.FileField(blank=False, null=True)
    transcript = models.FileField(blank=False, null=True)
    acceptance_letter = models.FileField(blank=False, null=True)
    passport = models.FileField(blank=False, null=True)
    university_fee_reciept = models.FileField(blank=False, null=True)
    embassy_fee_reciept = models.FileField(blank=False, null=True)
    insurance = models.FileField(blank=False, null=True)
    bank_statement = models.FileField(blank=False, null=True)
    flight_reservation = models.FileField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default="new",
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.passport_number


class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    #   file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50, null=True)
    e_mail = models.CharField(max_length=100, null=True)
    dath_of_birth = models.CharField(max_length=50, null=True)
    sponser = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    passport_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    image = models.ImageField(blank=False, null=True)
    cover_letter = models.FileField(blank=False, null=True)
    proof_of_accomodation = models.FileField(blank=False, null=True)
    passport = models.FileField(blank=False, null=True)
    flight_reservation = models.FileField(blank=False, null=True)
    embassy_fee_reciept = models.FileField(blank=False, null=True)
    insurance = models.FileField(blank=False, null=True)
    bank_statement = models.FileField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default="new",
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.passport_number


class Work(models.Model):
    id = models.AutoField(primary_key=True)
    #   file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50, null=True)
    e_mail = models.CharField(max_length=100, null=True)
    dath_of_birth = models.CharField(max_length=50, null=True)
    sponser = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    passport_number = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    image = models.ImageField(blank=False, null=True)
    legal_status = models.FileField(blank=False, null=True)
    economic_activity = models.FileField(blank=False, null=True)
    passport = models.FileField(blank=False, null=True)
    deed_for_company = models.FileField(blank=False, null=True)
    embassy_fee_reciept = models.FileField(blank=False, null=True)
    insurance = models.FileField(blank=False, null=True)
    bank_statement = models.FileField(blank=False, null=True)
    flight_reservation = models.FileField(blank=False, null=True)
    contract = models.FileField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=32,
        choices=STATUS,
        default="new",
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.passport_number


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    #   file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=50, null=True)
    e_mail = models.CharField(max_length=100, null=True)
    message = models.TextField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=32,
        choices=STATUS1,
        default="new",
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.e_mail
