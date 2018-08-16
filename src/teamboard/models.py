from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    user = models.OneToOneField(User, db_index=True, null=False, blank=False, unique=True, on_delete=models.CASCADE)
    uid = models.BigIntegerField(null=False, blank=False, unique=True)
    score = models.PositiveIntegerField(blank=False, default=0)
    banned = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{"[BANNED] " if self.banned else ""}{self.user}: {self.score}'
