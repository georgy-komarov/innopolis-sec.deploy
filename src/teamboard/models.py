import random

from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    user = models.OneToOneField(User, db_index=True, null=False, blank=False, unique=True, on_delete=models.CASCADE)
    uid = models.BigIntegerField(null=False, blank=False, unique=True, default=random.randrange(10 ** 12, 10 ** 13))
    score = models.PositiveIntegerField(blank=False, default=0)

    def __str__(self):
        return f'{self.user}: {self.score}'
