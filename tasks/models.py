from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    text         = models.CharField(unique=True, blank=False, null=False, max_length=60)
    completed    = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.text