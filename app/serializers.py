from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'image', 'image_url', 'body']

    def get_image_url(self, obj):
        if obj.image:
            # Assuming MEDIA_URL is '/media/' and obj.image.url is the relative path of the image
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None