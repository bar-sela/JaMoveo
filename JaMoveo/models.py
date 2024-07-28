from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    INSTRUMENT_CHOICES = [
        ('guitar', 'Guitar'),
        ('drums', 'Drums'),
        ('bass', 'Bass'),
        ('saxophone', 'Saxophone'),
        ('keyboard', 'Keyboard'),
        ('vocals', 'Vocals'),
    ]
    instrument = models.CharField(max_length=20, choices=INSTRUMENT_CHOICES, blank=True)
    is_admin = models.BooleanField(default=False)


