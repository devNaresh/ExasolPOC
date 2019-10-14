import glob
import os
import pandas as pd
import Utilities
import pyexasol
from sqlalchemy import create_engine,String,DateTime,Integer,DECIMAL, TEXT

engine = create_engine("mysql+pymysql://root:Rajendra@423@localhost:3306/poc")
#
# C = pyexasol.connect(dsn="localhost:8899", user="sys", password="exasol", schema="poc",
#                      compression=True)
pr_to_en_translation = pd.read_csv(f"{os.getcwd()}/data/train/product_category_name_translation_train.csv")
translations = pr_to_en_translation.set_index('product_category_name').to_dict()['product_category_name_english']
files = glob.glob(f"{os.getcwd()}/data/train/olist_*.csv")
datatypes = {
    'orders': {
        'order_id': String(100),
        'customer_id': String(100),
        'order_status': String(50),
        'order_purchase_timestamp': DateTime,
        'order_approved_at': DateTime,
        'order_delivered_carrier_date': DateTime,
        'order_delivered_customer_date': DateTime,
        'order_estimated_delivery_date': DateTime,
     },
    'customers':{
        'customer_id':String(100),
        'customer_unique_id':String(100),
        'customer_zip_code_prefix':Integer,
        'customer_city':String(50),
        'customer_state':String(5)
    },
    'order_items':{
        'order_id':String(100),
        'order_item_id':String(100),
        'product_id':String(100),
        'seller_id': String(100),
        'shipping_limit_date': DateTime,
        'price': DECIMAL(15,2),
        'freight_value':DECIMAL(15,2)
    },
    'order_payments':{
        'order_id':String(100),
        'payment_sequential': Integer,
        'payment_type': String(50),
        'payment_installments': Integer,
        'payment_value': DECIMAL(15,2)
    },
    'order_reviews':{
        'review_id':String(150),
        'order_id':String(100),
        'review_score':Integer,
        'review_comment_title':TEXT,
        'review_comment_message':TEXT,
        'review_creation_date': DateTime,
        'review_answer_timestamp': DateTime
    },
    'products':{
        'product_id':String(100),
        'product_category_name':String(200),
        'product_name_lenght': DECIMAL(15,2),
        'product_description_lenght': DECIMAL(15,2),
        'product_photos_qty': DECIMAL(15,2),
        'product_weight_g': DECIMAL(15,2),
        'product_length_cm':DECIMAL(15,2),
        'product_height_cm': DECIMAL(15,2),
        'product_width_cm': DECIMAL(15,2),
    },
    'sellers':{
        'seller_id':String(100),
        'seller_zip_code_prefix':Integer,
        'seller_city':String(100),
        'seller_state':String(10)
    }

}
@Utilities.measure_time
def load_to_mysql():
    for file in files:
        dataset_name = file.split('/')[-1][:-10]
        dataset_name = dataset_name.replace("olist_", '')
        dataset_name = dataset_name.replace("_dataset", "")
        df = pd.read_csv(file)
        if (dataset_name == 'products'):
            df['product_category_name'] = df['product_category_name'].apply(lambda x: translations.get(x, x))
        if (dataset_name == 'order_reviews' or dataset_name=='geolocation'):
            print('passed',dataset_name)
            pass
        else:
            df.to_sql(dataset_name, engine, if_exists="append", method="multi", index=False,dtype=datatypes.get(dataset_name, None))

@Utilities.measure_time
def load_to_exasol():
    for file in files:
        dataset_name = file.split('/')[-1][:-10]
        dataset_name = dataset_name.replace("olist_", '')
        dataset_name = dataset_name.replace("_dataset", "")
        df = pd.read_csv(file)
        if (dataset_name == 'products'):
            df['product_category_name'] = df['product_category_name'].apply(lambda x: translations.get(x, x))
        C.execute(pd.io.sql.get_schema(df, dataset_name.upper()).replace("TEXT", "VARCHAR(1000)"))
        C.import_from_pandas(df,dataset_name)

load_to_mysql()
# load_to_exasol()