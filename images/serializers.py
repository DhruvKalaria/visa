from django.core.mail import send_mail
from rest_framework import serializers
from .models import File, Tour, Work, Contact


class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model = File
        fields = ('degree', 'transcript', 'acceptance_letter', 'passport',
                  'university_fee_reciept', 'embassy_fee_reciept', 'insurance', 'bank_statement',
                  'image', 'name', 'e_mail', 'dath_of_birth', 'sponser', 'phone', 'passport_number', 'address',
                  'status', 'flight_reservation')


class FileSerializerTour(serializers.ModelSerializer):
    class Meta():
        model = Tour
        fields = ('cover_letter', 'proof_of_accomodation', 'flight_reservation', 'passport',
                  'embassy_fee_reciept', 'insurance', 'bank_statement',
                  'image', 'name', 'e_mail', 'dath_of_birth', 'sponser', 'phone', 'passport_number', 'address',
                  'status')


class FileSerializerWork(serializers.ModelSerializer):
    class Meta():
        model = Work
        fields = ('legal_status', 'economic_activity', 'deed_for_company', 'passport',
                  'embassy_fee_reciept', 'insurance', 'bank_statement',
                  'image', 'name', 'e_mail', 'dath_of_birth', 'sponser', 'phone', 'passport_number', 'address',
                  'flight_reservation', 'status', 'contract')


class FileSerializerContact(serializers.ModelSerializer):
    class Meta():
        model = Contact
        fields = ('name', 'e_mail', 'message'
                  )

    def send_dynamic_mail(self, serializers):
        from_email = 'syedamar.abbas555@gmail.com'
        send_mail('New Files have been Uploaded',
                  'New files have been uploaded.',
                  from_email,
                  [serializers.data.e_mail, ],
                  fail_silently=False)
