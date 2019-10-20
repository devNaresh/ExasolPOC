# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from model_utils.models import TimeStampedModel


class Aisles(TimeStampedModel):
    aisle_id = models.AutoField(primary_key=True)
    aisle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aisles'


class Departments(TimeStampedModel):
    department_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class OrderProducts(TimeStampedModel):
    order_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    add_to_cart_order = models.IntegerField(blank=True, null=True)
    reordered = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_products'


class Orders(TimeStampedModel):
    order_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    eval_set = models.TextField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    order_dow = models.IntegerField(blank=True, null=True)
    order_hour_of_day = models.IntegerField(blank=True, null=True)
    days_since_prior_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Products(TimeStampedModel):
    product_id = models.AutoField(primary_key=True)
    product_name = models.TextField(blank=True, null=True)
    aisle_id = models.BigIntegerField(blank=True, null=True)
    department_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'
