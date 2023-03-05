from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    points = models.PositiveIntegerField(default=0)
    test_1 = models.BooleanField(default=False)
    test_2 = models.BooleanField(default=False)
    test_3 = models.BooleanField(default=False)
    test_4 = models.BooleanField(default=False)
    test_5 = models.BooleanField(default=False)
    test_6 = models.BooleanField(default=False)
    test_7 = models.BooleanField(default=False)
    test_8 = models.BooleanField(default=False)
    art_2 = models.BooleanField(default=False)
    art_3 = models.BooleanField(default=False)
    art_4 = models.BooleanField(default=False)
    art_5 = models.BooleanField(default=False)
    art_6 = models.BooleanField(default=False)
