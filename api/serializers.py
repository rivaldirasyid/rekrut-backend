from rest_framework import serializers
from .models import Kandidat, Kriteria

class KriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kriteria
        fields = '__all__'

class KandidatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kandidat
        fields = '__all__'
