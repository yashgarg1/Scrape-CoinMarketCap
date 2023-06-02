from django.db import models

# Create a model for the cryptocurrency data.
class Cryptocurrency(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    one_h_percent = models.FloatField()
    twentyFour_h_percent = models.FloatField()
    seven_d_percent = models.FloatField()
    market_cap = models.FloatField()
    volume_24h = models.FloatField()
    circulating_supply = models.FloatField()