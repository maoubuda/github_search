from django.db import models


class Repos(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=50,
        null=False,
        blank=True)

    name = models.CharField(
        max_length=50,
        null=False,
        blank=False)
