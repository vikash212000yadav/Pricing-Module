from django.db import models


# Create your models here.

class Constraints(models.Model):
    # id = models.IntegerField(primary_key=True)
    distance_covered = models.IntegerField()
    time_taken = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
