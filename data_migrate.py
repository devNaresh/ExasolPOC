#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import glob
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split


# In[71]:


engine = create_engine("mysql+pymysql://root:testsql@localhost/testing")


# In[72]:


files = glob.glob("/Users/nareshkumar/Desktop/brazilian-ecommerce/train/*.csv")


# In[73]:


for file in files:
    df = pd.read_csv(file)
    df.to_sql(file.split('/')[-1][:-14], engine, if_exists="append")


# In[ ]:




