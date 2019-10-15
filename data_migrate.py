import glob
import os
import pandas as pd
import numpy as np
import Utilities
import pyexasol
import pymysql.cursors
from sqlalchemy import create_engine,String,DateTime,Integer,DECIMAL, TEXT

engine = create_engine("mysql+pymysql://root:testsql@localhost/testing")
engine_exa = create_engine("exa+turbodbc://sys:exasol@127.0.0.1:8899/ecom?CONNECTIONLCALL=en_US.UTF-8&driver=EXASolution Driver", echo=False)

C = pyexasol.connect(dsn="localhost:8899", user="sys", password="exasol", schema="poc", compression=True)
                     
files = glob.glob(f"{os.getcwd()}/data/*.csv")
datatypes = {
    'aisles': {
        'aisles_id': Integer(),
        'aisle': String(100)
     },
    'departments':{
        'department_id':Integer(),
        'department':String(100)
    },
    'order_products':{
        'order_id':Integer(),
        'product_id':Integer(),
        'add_to_cart_order':Integer(),
        'reordered': Integer()
    },
    'orders':{
        'order_id':Integer(),
        'user_id': Integer(),
        'order_number': Integer(),
        'order_dow': Integer(),
        'order_hour_of_day': Integer(),
        'days_since_prior_order': Integer(),
        'order_date': DateTime()
    },
    'products':{
        'product_id':Integer(),
        'product_name':TEXT(),
        'aisle':Integer(),
        'department':Integer()
    }
}


@Utilities.measure_time
def load_to_mysql():
    for file in files:
        dataset_name = file.split('/')[-1][:-4]
        df = pd.read_csv(file)
        df.replace(np.nan, 0, inplace=True)
        if ("order_products" in dataset_name):
            dataset_name = dataset_name.split('__')[0]
        # df.to_sql(dataset_name, engine, if_exists="append", index=False,dtype=datatypes.get(dataset_name, None))

        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='testsql',
                                    db='testing',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                sql = f"INSERT INTO {dataset_name} ({', '.join(df.columns)}) VALUES ({('%s, '*len(df.columns))[:-2]})"
                stmt = f"SHOW TABLES LIKE '{dataset_name}'"
                cursor.execute(stmt)
                result = cursor.fetchone()
                if not result:
                    cursor.execute(pd.io.sql.get_schema(df, dataset_name, con=engine, dtype=datatypes.get(dataset_name)))
                cursor.executemany(sql, [tuple(x) for x in df.values.tolist()])
            connection.commit()
        finally:
            connection.close()

@Utilities.measure_time
def load_to_exasol():
    for file in files:
        dataset_name = file.split('/')[-1][:-4]
        df = pd.read_csv(file)
        if ("order_products" in dataset_name):
            dataset_name = dataset_name.split('__')[0]
        if not C.ext.get_sys_tables(table_name_prefix=dataset_name):
            C.execute(pd.io.sql.get_schema(df, dataset_name, con=engine_exa, dtype=datatypes.get(dataset_name)).replace("TEXT", "VARCHAR(1000)"))
        C.import_from_pandas(df, dataset_name)

load_to_mysql()
load_to_exasol()