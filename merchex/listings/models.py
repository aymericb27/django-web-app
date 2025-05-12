from django.db import models

class Band(models.model):
    name = models.fields.CharField(max_length=100)
