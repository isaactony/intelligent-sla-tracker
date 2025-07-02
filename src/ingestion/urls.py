from django.urls import path
from .views import (
    TicketEventIngestView,
    TicketEventListView,
    TicketEventDetailView,
)

urlpatterns = [
    # POST /api/v1/ticket-events/
    path('ticket-events/', TicketEventIngestView.as_view(), name='ticket-event-ingest'),
    # GET /api/v1/ticket-events/
    path('ticket-events/list/', TicketEventListView.as_view(), name='ticket-event-list'),
    # GET /api/v1/ticket-events/<int:pk>/
    path('ticket-events/<int:pk>/', TicketEventDetailView.as_view(), name='ticket-event-detail'),
]