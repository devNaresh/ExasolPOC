# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customers(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    customer_id = models.TextField(primary_key=True, null=False)
    customer_unique_id = models.TextField(blank=True, null=True)
    customer_zip_code_prefix = models.BigIntegerField(blank=True, null=True)
    customer_city = models.TextField(blank=True, null=True)
    customer_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Geolocation(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    geolocation_zip_code_prefix = models.BigIntegerField(primary_key=True, null=False)
    geolocation_lat = models.FloatField(blank=True, null=True)
    geolocation_lng = models.FloatField(blank=True, null=True)
    geolocation_city = models.TextField(blank=True, null=True)
    geolocation_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geolocation'


class OrderItems(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    order_id = models.TextField(blank=True, null=True)
    order_item_id = models.BigIntegerField(primary_key=True, null=False)
    product_id = models.TextField(blank=True, null=True)
    seller_id = models.TextField(blank=True, null=True)
    shipping_limit_date = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    freight_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_items'


class OrderPayments(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    order_id = models.TextField(blank=True, null=True)
    payment_sequential = models.BigIntegerField(primary_key=True, null=False)
    payment_type = models.TextField(blank=True, null=True)
    payment_installments = models.BigIntegerField(blank=True, null=True)
    payment_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_payments'


class OrderReviews(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    review_id = models.TextField(primary_key=True,null=False)
    order_id = models.TextField(blank=True, null=True)
    review_score = models.TextField(blank=True, null=True)
    review_comment_title = models.TextField(blank=True, null=True)
    review_comment_message = models.TextField(blank=True, null=True)
    review_creation_date = models.TextField(blank=True, null=True)
    review_answer_timestamp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_reviews'


class Orders(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    order_id = models.TextField(primary_key=True, null=False)
    customer_id = models.TextField(blank=True, null=True)
    order_status = models.TextField(blank=True, null=True)
    order_purchase_timestamp = models.TextField(blank=True, null=True)
    order_approved_at = models.TextField(blank=True, null=True)
    order_delivered_carrier_date = models.TextField(blank=True, null=True)
    order_delivered_customer_date = models.TextField(blank=True, null=True)
    order_estimated_delivery_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Products(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    product_id = models.TextField(primary_key=True,null=False)
    product_category_name = models.TextField(blank=True, null=True)
    product_name_lenght = models.FloatField(blank=True, null=True)
    product_description_lenght = models.FloatField(blank=True, null=True)
    product_photos_qty = models.FloatField(blank=True, null=True)
    product_weight_g = models.FloatField(blank=True, null=True)
    product_length_cm = models.FloatField(blank=True, null=True)
    product_height_cm = models.FloatField(blank=True, null=True)
    product_width_cm = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'

class Sellers(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    seller_id = models.TextField(primary_key=True,null=False)
    seller_zip_code_prefix = models.BigIntegerField(blank=True, null=True)
    seller_city = models.TextField(blank=True, null=True)
    seller_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sellers'
