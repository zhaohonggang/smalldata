from django.db import models

# Create your models here.
class SoldSummary(models.Model):
    city = models.CharField(max_length=1000, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=1000, blank=True, null=True)
    year = models.FloatField(blank=True, null=True)
    month = models.FloatField(blank=True, null=True)
    total = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    count = models.BigIntegerField(blank=True, null=True)
    prices = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'vw_sum_sold'

class HouseCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    en = models.CharField(max_length=500, blank=True, null=True)
    cn = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_category'

class CityArea(models.Model):
    city = models.CharField(max_length=500, blank=True, null=True)
    area = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_city_area'

