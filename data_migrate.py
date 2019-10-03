import pandas as pd
import glob
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split


engine = create_engine("mysql+pymysql://root:testsql@localhost/testing")

files = glob.glob(f"{os.getcwd()}/data/train/*.csv")


for file in files:
    df = pd.read_csv(file)
    df.to_sql(file.split('/')[-1][:-10], engine, if_exists="append", method="multi")


## To transfer data in Exasol

C = pyexasol.connect(dsn="localhost:8899", user="sys", password="exasol", schema="PUBLIC",
                     compression=True)
for file in files:
    df = pd.read_csv(file)
    C.execute(pd.io.sql.get_schema(df, file.split('/')[-1][:-10].upper()).replace("TEXT", "VARCHAR(1000)"))
    C.import_from_pandas(df, file.split('/')[-1][:-10])
