from sqlalchemy import Column, Float, Integer, String, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_orders = Table(
    'orders', metadata,
    Column('id', Integer, primary_key=True),
    Column('order_id', String(50)),
    Column('status', String(50)),
    Column('payment_id', Integer),
    Column('product_id', Integer),
    Column('seller_id', Integer),
    Column('date_id', Integer),
    Column('customer_id', Integer),
    Column('items', Integer)
)


t_datedm = Table(
    'datedm', metadata,
    Column('id', Integer, primary_key=True),
    Column('purchase_date', DateTime),
    Column('approved_date', DateTime),
    Column('delivered_carrier_date', DateTime),
    Column('delivered_customer_date', DateTime),
    Column('estimate_delivery_date', DateTime),
    Column('shipping_limit_date', DateTime)
)


t_payments = Table(
    'payments', metadata,
    Column('id', Integer, primary_key=True),
    Column('payment_type', String(50)),
    Column('installments', Integer),
    Column('payment_value', Float)
)

t_product = Table(
    'product', metadata,
    Column('id', Integer, primary_key=True),
    Column('idd', String(50)),
    Column('category', String(50)),
    Column('price', Float),
    Column('freight_value', Float)
)

t_user = Table(
    'USER', metadata,
    Column('id', Integer, primary_key=True),
    Column('idd', String(50)),
    Column('zipcode', String(50)),
    Column('city', String(50)),
    Column('user_state', String(50))
)