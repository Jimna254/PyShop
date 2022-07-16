from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2048)
   
    def __str__(self):
        return self.name


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='20% off')
    discount = models.FloatField(default=0.2)
  
    def __str__(self):
        return self.code
        