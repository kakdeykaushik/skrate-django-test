from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Ticket(models.Model):
    class Status(models.TextChoices):
        OPEN = "O", _("Open")
        CLOSED = "C", _("Closed")

    class Priority(models.TextChoices):
        LOW = "L", _("Low")
        MEDIUM = "M", _("Medium")
        HIGH = "H", _("High")

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.OPEN)
    priority = models.CharField(
        max_length=1, choices=Priority.choices, default=Priority.LOW
    )
    assignedTo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createAt = models.DateTimeField(auto_now_add=True)
