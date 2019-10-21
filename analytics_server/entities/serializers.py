from rest_framework import serializers
from entities import models


class AisleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aisles
        fields = '__all__'


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departments
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Orders
        fields = '__all__'


class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderProducts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'
