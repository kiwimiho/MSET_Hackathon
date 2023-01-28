from django.db import models
from django.utils import timezone

# Create your models here.


class WellBeing(models.Model):
    date = models.DateTimeField(default=timezone.now)

    # additional field for User
    mood = models.CharField(max_length=128)

    activity = models.CharField(max_length=128)

    def __str__(self):
        return self.mood