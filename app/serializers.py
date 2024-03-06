from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'image', 'image_url', 'body']

    def create(self, validated_data):
        image_url = None
        image = validated_data.get('image')  # Get the 'image' file object from validated data
        if image:  # Check if 'image' file object exists
            image_url = image  # Get the URL of the uploaded image
        validated_data['image_url'] = image_url  # Assign the URL to 'image_url' field in validated data
        return super().create(validated_data)