from rest_framework import generics, status
from .models import Event
from .serializers import EventSerializer
from django.shortcuts import get_object_or_404, render
from django.urls import get_resolver
from rest_framework.response import Response



# this function is made to display the list of apis in the homepage of this project
def api_list(request):
    url_list = []
    for url_pattern in get_resolver().reverse_dict.keys():
        if isinstance(url_pattern, str) and url_pattern.startswith('api:'):
            url_list.append(url_pattern.replace('api:', ''))
    return render(request, 'index.html', {'url_list': url_list})

'''this api is to fetch the all the events from the database '''
class EventDetailListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.order_by('-date')

'''this api is to fecth the specific events from the database '''  
class EventRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = EventSerializer

    def get_object(self):
        return get_object_or_404(Event, pk=self.kwargs.get('pk'))

'''this is api to create the new events in our database'''
class EventCreateAPIView(generics.CreateAPIView):
    queryset = Event.objects.none()  # Empty queryset
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
'''this is api to update the existing events in our database if there any'''

class EventUpdateAPIView(generics.UpdateAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        event_id = self.kwargs.get('pk')
        return Event.objects.filter(pk=event_id)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''this is api to delete the existing events in our database if there any'''

class EventDeleteAPIView(generics.DestroyAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        event_id = self.kwargs.get('pk')
        return Event.objects.filter(pk=event_id)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.delete()
            return Response({"message": "Event deleted sucessfully"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)