import graphene
from graphene import relay,ObjectType
from graphene_django.types import DjangoObjectType

from entities.models import Aisles,Departments,Products,OrderProducts,Orders
from graphene_django.filter import DjangoFilterConnectionField

class AisleNode(DjangoObjectType):
    class Meta:
        model = Aisles
        filter_fields = []
        interfaces = (relay.Node,)
class DepartmentNode(DjangoObjectType):
    class Meta:
        model = Departments
        filter_fields=[]
        interfaces = (relay.Node,)
class ProductNode(DjangoObjectType):
    class Meta:
        model = Products
        filter_fields = []
        interfaces =(relay.Node,)

class OrderProductNode(DjangoObjectType):
    class Meta:
        model= OrderProducts
        filter_fields = []
        interfaces = (relay.Node,)

class OrderNode(DjangoObjectType):
    class Meta:
        model = Orders
        filter_fields = ['order_dow', 'order_hour_of_day', 'days_since_prior_order']
        interfaces = (relay.Node,)

class Query(ObjectType):
    product = relay.Node.Field(ProductNode)
    all_products = DjangoFilterConnectionField(ProductNode)

    aisle = relay.Node.Field(AisleNode)
    all_aisle= DjangoFilterConnectionField(AisleNode)

    order = relay.Node.Field(OrderNode)
    all_orders = DjangoFilterConnectionField(OrderNode)

    orderproduct = relay.Node.Field(OrderProductNode)
    all_orderproducts = DjangoFilterConnectionField(OrderProductNode)

    department = relay.Node.Field(DepartmentNode)
    all_departments = DjangoFilterConnectionField(DepartmentNode)





schema = graphene.Schema(query=Query)
