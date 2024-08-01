import uuid
from django.db import models

class TrackingNumber(models.Model):
    id = models.BigAutoField(primary_key=True)  # Auto-incrementing ID
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uuid)

    class Meta:
        db_table = 'tracking_numbers'
