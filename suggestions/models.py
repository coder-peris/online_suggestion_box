from django.db import models

# Create your models here.
from django.db import models


class Suggestion(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    suggestion = models.TextField()
    notification = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if (self.name):
            return self.name
        else:
            return "Anonymous"