import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import select

from models import *

engine = create_engine("mysql+pymysql://root:testsql@localhost/testing")
engine_exa = create_engine(
    "exa+turbodbc://sys:exasol@127.0.0.1:8899/ecom?CONNECTIONLCALL=en_US.UTF-8&driver=EXASolution Driver", echo=False)

# create connection
conn = engine_exa.connect()

# ETL users data
df_customers = pd.read_sql("select * from olist_customers_dataset", engine)
df_sellers = pd.read_sql("select * from olist_sellers_dataset", engine)
df_customers = df_customers[["customer_id", "customer_zip_code_prefix",
                             "customer_city", "customer_state"]].rename(columns={"customer_id": "idd",
                                                                                 "customer_city": "city",
                                                                                 "customer_state": "user_state",
                                                                                 "customer_zip_code_prefix": "zipcode"})
df_sellers = df_sellers.rename(columns={"seller_id": "idd",
                                        "seller_city": "city",
                                        "seller_state": "user_state",
                                        "seller_zip_code_prefix": "zipcode"})
df_users = pd.concat([df_customers, df_sellers])
conn.execute(t_user.insert(), df_users.to_dict(orient="records"))
print("Users Load Done")

# ETL Products Data
df_products = pd.read_sql("select * from olist_products_dataset", engine)
df_items = pd.read_sql("select product_id, price, freight_value from olist_order_items_dataset", engine)
df_items = df_items.drop_duplicates(subset="product_id", keep="first")
df_products = df_products[["product_id", "product_category_name"]]
df_products = df_products.merge(df_items, on="product_id").rename(columns={
    "product_id": "idd",
    "product_category_name": "category"
})
conn.execute(t_product.insert(), df_products.to_dict(orient="records"))
print("Products Load Done")


# ETL Orders Data
df_payments = pd.read_sql("select * from olist_order_payments_dataset", engine)
df_orders = pd.read_sql("select * from olist_orders_dataset", engine)
df_items = pd.read_sql(
    "select order_id, product_id, seller_id, order_item_id, shipping_limit_date from olist_order_items_dataset", engine)

df_orders = df_orders.merge(df_payments, on="order_id")
df_orders = df_orders.merge(df_items, on="order_id")

for i in range(50000):      # Change Num of orders
    obj = df_orders.iloc[i].to_dict()
    order_obj = dict()
    try:
        date_obj = t_datedm.insert().values(purchase_date=obj["order_purchase_timestamp"],
                                            approved_date=obj["order_approved_at"],
                                            delivered_carrier_date=obj["order_delivered_carrier_date"],
                                            delivered_customer_date=obj["order_delivered_customer_date"],
                                            estimate_delivery_date=obj["order_estimated_delivery_date"],
                                            shipping_limit_date=obj["shipping_limit_date"])

        date_id = conn.execute(date_obj).inserted_primary_key[0]
        payments_obj = {
            "payment_type": obj["payment_type"],
            "installments": obj["payment_installments"],
            "payment_value": obj["payment_value"]
        }
        payment_id = conn.execute(t_payments.insert().values(**payments_obj)).inserted_primary_key[0]

        with engine_exa.begin() as conn_1:
            user_id = conn_1.execute(select([t_user.c.id]).where(t_user.c.idd == obj.get("customer_id"))).first()
            seller_id = conn_1.execute(select([t_user.c.id]).where(t_user.c.idd == obj.get("seller_id"))).first()
            product_id = conn_1.execute(
                select([t_product.c.id]).where(t_product.c.idd == obj.get("product_id"))).first()

            if user_id:
                order_obj["customer_id"] = user_id[0]
            if seller_id:
                order_obj["seller_id"] = seller_id[0]
            if product_id:
                order_obj["product_id"] = product_id[0]

            order_obj["date_id"] = date_id
            order_obj["order_id"] = obj["order_id"]
            order_obj["status"] = obj["order_status"]
            order_obj["items"] = obj["order_item_id"]
            order_obj["payment_id"] = payment_id
            conn_1.execute(t_orders.insert().values(**order_obj))

    except Exception as e:
        print(e)
        conn.execute(t_datedm.delete().where(t_datedm.c.id == date_id))
        conn.execute(t_payments.delete().where(t_payments.c.id == payment_id))
