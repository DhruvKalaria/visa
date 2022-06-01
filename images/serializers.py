from rest_framework import serializers
from .models import File, Tour

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('degree', 'transcript', 'acceptance_letter','passport',
     'university_fee_reciept', 'embassy_fee_reciept','insurance', 'bank_statement',
     'image', 'name','e_mail', 'dath_of_birth','sponser','phone','passport_number','address',
      'timestamp')

class FileSerializerTour(serializers.ModelSerializer):
  class Meta():
    model = Tour
    fields = ('cover_letter', 'proof_of_accomodation', 'flight_reservation','passport',
    'embassy_fee_reciept','insurance', 'bank_statement',
     'image', 'name','e_mail', 'dath_of_birth','sponser','phone','passport_number','address',
      'timestamp')