from rest_framework import generics
from .models import TicketEvent
from .serializers import TicketEventSerializer

class TicketEventIngestView(generics.CreateAPIView):
    queryset = TicketEvent.objects.all()
    serializer_class = TicketEventSerializer

class TicketEventListView(generics.ListAPIView):
    queryset = TicketEvent.objects.all()
    serializer_class = TicketEventSerializer

class TicketEventDetailView(generics.RetrieveAPIView):
    queryset = TicketEvent.objects.all()
    serializer_class = TicketEventSerializer