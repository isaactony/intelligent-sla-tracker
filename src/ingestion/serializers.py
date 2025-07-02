from rest_framework import serializers
from .models import TicketEvent

class TicketEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketEvent
        fields = '__all__'