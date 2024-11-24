# api/serializers.py

from rest_framework import serializers
from .models import MNStatus

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = MNStatus
        fields = ('id', 'Temp', 'Humi', 'Volt', 'date_updated')