from django.db import models
import uuid


class Server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    members_count = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)