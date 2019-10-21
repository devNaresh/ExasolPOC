from graphene_django.rest_framework.mutation import SerializerMutation
from entities import serializers


class AislesMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.AisleSerializer


class DepartmentsMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.DepartmentsSerializer


class OrderProductsMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.OrderProductsSerializer


class OrdersMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.OrdersSerializer


class ProductsMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.ProductsSerializer