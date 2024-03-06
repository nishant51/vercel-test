from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'image', 'body']