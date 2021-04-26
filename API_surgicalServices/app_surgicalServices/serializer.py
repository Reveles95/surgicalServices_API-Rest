from rest_framework import serializers
from .models import * 

class specialistsTeam_serializer(serializers.ModelSerializer):
    class Meta:
        model =  specialistsTeam
        fields = '__all__'

class Services_serializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'