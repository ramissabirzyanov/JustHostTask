from django.db import models
import uuid


class VPS(models.Model):
    STATUS_TYPES = [
        ('started', 'STARTED'),
        ('blocked', 'BLOCKED'),
        ('stopped', 'STOPPED'),
    ]
    uid = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    cpu = models.PositiveIntegerField()
    ram = models.PositiveIntegerField()
    hdd = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS_TYPES, default='started')

    class Meta:
        db_table = 'vps'
        verbose_name = 'vps'

    def __str__(self):
        return f"VPS {self.uid} ({self.status})"
