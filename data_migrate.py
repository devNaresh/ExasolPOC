import glob
import os
import pandas as pd
import Utilities
import pyexasol
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Rajendra@423@localhost:3306/poc")

C = pyexasol.connect(dsn="localhost:8899", user="sys", password="exasol", schema="poc",
                     compression=True)
pr_to_en_translation = pd.read_csv(f"{os.getcwd()}/data/train/product_category_name_translation_train.csv")
translations = pr_to_en_translation.set_index('product_category_name').to_dict()['product_category_name_english']
files = glob.glob(f"{os.getcwd()}/data/train/olist_*.csv")

@Utilities.measure_time
def load_to_mysql():
    for file in files:
        dataset_name = file.split('/')[-1][:-10]
        dataset_name = dataset_name.replace("olist_", '')
        dataset_name = dataset_name.replace("_dataset", "")
        df = pd.read_csv(file)
        if (dataset_name == 'products'):
            df['product_category_name'] = df['product_category_name'].apply(lambda x: translations.get(x, x))
        df.to_sql(dataset_name, engine, if_exists="append", method="multi")

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
load_to_exasol()