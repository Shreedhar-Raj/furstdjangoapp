from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField()
    price = models.FloatField()
    stock = models.IntegerField()
    img_url = models.CharField()