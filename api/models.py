from django.db import models


class UserInput(models.Model):
    budget = models.IntegerField()
    available_from = models.CharField(max_length=50)
    available_to = models.CharField(max_length=50)
