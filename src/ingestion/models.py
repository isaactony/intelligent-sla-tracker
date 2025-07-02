from django.db import models

class TicketEvent(models.Model):
    ticket_id = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket_id} - {self.event_type}"

    class Meta:
        db_table = 'ticket_event'