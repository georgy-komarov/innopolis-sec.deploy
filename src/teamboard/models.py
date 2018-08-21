from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField(db_index=True, max_length=50, null=False, blank=False, unique=True)
    invite = models.CharField(max_length=64, null=False, blank=False)
    uid = models.BigIntegerField(null=False, blank=False, unique=True)
    score = models.PositiveIntegerField(blank=False, default=0)
    banned = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return str(self.user)
