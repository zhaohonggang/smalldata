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

'''
python manage.py inspectdb --database realtor > realtorModels.py
'''
class CityArea(models.Model):
    city = models.CharField(max_length=500, blank=True, null=True)
    area = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_city_area'

class HouseForSale(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mlsno = models.CharField(unique=True, max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    stno = models.CharField(max_length=100, blank=True, null=True)
    stname = models.CharField(max_length=100, blank=True, null=True)
    sttype = models.CharField(max_length=100, blank=True, null=True)
    aptno = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    askprice = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    soldprice = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    solddate = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    style = models.CharField(max_length=100, blank=True, null=True)
    bdrm = models.IntegerField(blank=True, null=True)
    wshrm = models.IntegerField(blank=True, null=True)
    maint = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=14, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=14, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_for_sale'


class HouseSold(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mlsno = models.CharField(unique=True, max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    stno = models.CharField(max_length=100, blank=True, null=True)
    stname = models.CharField(max_length=100, blank=True, null=True)
    sttype = models.CharField(max_length=100, blank=True, null=True)
    aptno = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    askprice = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    inputdate = models.DateField(blank=True, null=True)
    soldprice = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    solddate = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    style = models.CharField(max_length=100, blank=True, null=True)
    bdrm = models.IntegerField(blank=True, null=True)
    wshrm = models.IntegerField(blank=True, null=True)
    maint = models.DecimalField(max_digits=18, decimal_places=4, blank=True, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=14, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=14, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_sold'