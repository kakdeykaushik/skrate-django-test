from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

ADMIN = 1
EMPLOYEE = 2

ROLE_CHOICES = (
    (ADMIN, "Admin"),
    (EMPLOYEE, "Employee"),
)


class User(AbstractUser):

    username = models.CharField(max_length=20, unique=True, blank=False, null=False)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, blank=False, null=False
    )
    password = None

    REQUIRED_FIELDS = ["role"]  # username is by default set to required by Django

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)

        username = self.username
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"Username '{username}' is already in use.")

        int_roles = list(map(lambda x: x[0], ROLE_CHOICES))
        if self.role not in int_roles:
            raise ValidationError("Invalid Role")

    def save(self, *args, **kwargs):
        self.clean_fields()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.role}"
