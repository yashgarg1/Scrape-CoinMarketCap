from django.db import models

# Create a model for the cryptocurrency data.
class Cryptocurrency(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    one_h_percent = models.CharField(max_length=255)
    twentyFour_h_percent = models.CharField(max_length=255)
    seven_d_percent = models.CharField(max_length=255)
    market_cap = models.CharField(max_length=255)
    volume_24h = models.CharField(max_length=255)
    circulating_supply = models.CharField(max_length=255)