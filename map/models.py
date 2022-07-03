from django.db import models

# Create your models here.

from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField()

class latlon(models.Model):
    id = models.IntegerField(primary_key = True)
    lat = models.FloatField()
    lon = models.FloatField()

class heat_read(models.Model):
    id = models.IntegerField(primary_key = True)
    lat = models.FloatField()
    lon = models.FloatField()

class heat_orange(models.Model):
    id = models.IntegerField(primary_key = True)
    lat = models.FloatField()
    lon = models.FloatField()
