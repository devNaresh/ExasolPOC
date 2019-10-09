import graphene
from graphene import relay,ObjectType
from graphene_django.types import DjangoObjectType

from entities.models import Products,Sellers,Customers,Geolocation,OrderItems,OrderPayments,OrderReviews,Orders
from graphene_django.filter import DjangoFilterConnectionField

class CustomerNode(DjangoObjectType):
    class Meta:
        model = Customers
        filter_fields=['customer_zip_code_prefix','customer_city','customer_state']
        interfaces = (relay.Node,)
class GeolocationNode(DjangoObjectType):
    class Meta:
        model = Geolocation
        filter_fields = ['geolocation_city','geolocation_state']
        interfaces = (relay.Node,)
class OrderItemNode(DjangoObjectType):
    class Meta:
        model = OrderItems
        filter_fields = []
        interfaces =(relay.Node,)

class OrderPaymentNode(DjangoObjectType):
    class Meta:
        model= OrderPayments
        filter_fields = []
        interfaces = (relay.Node,)

class OrderReviewNode(DjangoObjectType):
    class Meta:
        model = OrderReviews
        filter_fields = []
        interfaces = (relay.Node,)

class OrderNode(DjangoObjectType):
    class Meta:
        model = Orders
        filter_fields = ['order_status']
        interfaces = (relay.Node,)


class ProductNode(DjangoObjectType):
    class Meta:
        model = Products
        filter_fields = ['product_category_name','product_weight_g','product_length_cm','product_height_cm','product_width_cm']
        interfaces = (relay.Node,)

class SellerNode(DjangoObjectType):
    class Meta:
        model = Sellers
        filter_fields = ['seller_city','seller_state','seller_zip_code_prefix']
        interfaces = (relay.Node,)

class Query(ObjectType):
    product = relay.Node.Field(ProductNode)
    all_products = DjangoFilterConnectionField(ProductNode)

    seller = relay.Node.Field(SellerNode)
    all_sellers = DjangoFilterConnectionField(SellerNode)

    order = relay.Node.Field(OrderNode)
    all_orders = DjangoFilterConnectionField(OrderNode)

    orderitem = relay.Node.Field(OrderItemNode)
    all_orderitems = DjangoFilterConnectionField(OrderItemNode)

    geolocation = relay.Node.Field(GeolocationNode)
    all_geolocations = DjangoFilterConnectionField(GeolocationNode)

    orderpayment = relay.Node.Field(OrderPaymentNode)
    all_orderpayments = DjangoFilterConnectionField(OrderPaymentNode)

    orderreview = relay.Node.Field(OrderReviewNode)
    all_orderreviews = DjangoFilterConnectionField(OrderReviewNode)




schema = graphene.Schema(query=Query)
