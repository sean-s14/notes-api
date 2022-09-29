from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    text         = models.CharField(unique=True, blank=False, null=False, max_length=60)
    completed    = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
<<<<<<< HEAD
        return self.text
=======
        return self.title
>>>>>>> b1f76a6887218d337153ed3a83957055c90efa50
