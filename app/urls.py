from django.urls import path
from .views import EventDetailListAPIView,EventRetrieveAPIView,EventCreateAPIView,EventUpdateAPIView,EventDeleteAPIView


urlpatterns = [
    path('events/detail/', EventDetailListAPIView.as_view(), name='event-list-api'),
    path('events/<int:pk>/', EventRetrieveAPIView.as_view(), name='event-detail'),
    path('events/create/', EventCreateAPIView.as_view(), name='event-create'),
    path('events/update/<int:pk>/', EventUpdateAPIView.as_view(), name='event-update'),
    path('events/delete/<int:pk>/', EventDeleteAPIView.as_view(), name='event-update'),



]