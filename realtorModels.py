# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    article_id = models.BigAutoField(primary_key=True)
    article_name = models.CharField(max_length=20)
    article_desc = models.TextField()
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'


class CondoSold(models.Model):
    id = models.BigAutoField(primary_key=True)
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
        db_table = 'condo_sold'


class House(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)
    img = models.CharField(max_length=1000, blank=True, null=True)
    price_str = models.CharField(max_length=1000, blank=True, null=True)
    mls_number = models.CharField(max_length=1000, blank=True, null=True)
    bed_str = models.CharField(max_length=1000, blank=True, null=True)
    bath_str = models.CharField(max_length=1000, blank=True, null=True)
    property_type = models.CharField(max_length=1000, blank=True, null=True)
    building_type = models.CharField(max_length=1000, blank=True, null=True)
    land_size = models.CharField(max_length=1000, blank=True, null=True)
    storeys = models.CharField(max_length=1000, blank=True, null=True)
    salesperson = models.CharField(max_length=1000, blank=True, null=True)
    brokerage = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house'


class HouseCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    en = models.CharField(max_length=500, blank=True, null=True)
    cn = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_category'


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


class HouseSoldBak(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    mlsno = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    stno = models.CharField(max_length=100, blank=True, null=True)
    stname = models.CharField(max_length=100, blank=True, null=True)
    sttype = models.CharField(max_length=100, blank=True, null=True)
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
    latitude = models.DecimalField(max_digits=18, decimal_places=14, blank=True, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=14, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house_sold_bak'
