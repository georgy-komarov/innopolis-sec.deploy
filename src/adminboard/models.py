from django.db import models


class Tag(models.Model):
    name = models.TextField(max_length=15, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(db_index=True, max_length=100, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=False)
    flag = models.CharField(max_length=50, null=False, blank=False, unique=True)
    points = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
