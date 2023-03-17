from django.db import models

# Create your models here.

class Item(models.Model):
    fruit_name = models.CharField(max_length=100)
    item = models.TextField()