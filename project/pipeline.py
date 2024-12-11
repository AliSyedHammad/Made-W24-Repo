#!/usr/bin/env python
# coding: utf-8

# ## Importing Python Packages

# In[2]:


import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import datetime as dt


# ## Loading the 311 Dataset

# In[3]:


df = pd.read_csv('311_Service_Requests_from_2010_to_Present_20241111.csv')


# ## Preprocessing the 311 Data

# Checking the loaded data

# In[4]:


pd.set_option('display.max_columns', None)
df.head(5)


# Listing the columns against their indexes

# In[5]:


count = 0
for col in df.columns:
  print(count, col)
  count+=1


# Dropping unnecessary columns to speed up data processing

# In[6]:


df.drop(df.columns[[32,33,34,35]], axis = 1, inplace = True) 


# Checking the shape and dataframe after dropping the columns

# In[7]:


print(df.shape)
df.head(5)


# Checking for nulls

# In[8]:


null_counts = df.isnull().sum()
print(null_counts)


# Checking datatypes

# In[9]:


print(df.dtypes)


# Converting datatypes for datetimes columns from object to datetime

# In[10]:


df['Closed Date']= pd.to_datetime(df['Closed Date'])
df['Created Date']= pd.to_datetime(df['Created Date'])


# Calculating Resolution Time and adding it to the dataframe

# In[11]:


df['Resolution_Time'] = (df['Closed Date'] - df['Created Date']).dt.days    


# Applying data sanity checks

# In[12]:


df = df[df['Resolution_Time'].notnull()]
df = df[df['Closed Date'] >= df['Created Date']]


# Creating new columns for day/week/ month/ year of the creation date

# In[13]:


df['Day of Week'] = df['Created Date'].dt.dayofweek
df['Day of Month'] = df['Created Date'].dt.day
df['Month'] = df['Created Date'].dt.month
df['Year'] = df['Created Date'].dt.year


# Checking the final data types

# In[14]:


df.dtypes


# ## Loading the Storms Dataset

# Loading the dataset for Bronx

# In[15]:


df_storm_bronx = pd.read_csv('storm_data_search_results_bronx.csv', 
                       header = 0,
                       sep = ',', 
                       parse_dates = ['BEGIN_DATE'],
                       index_col = 'EVENT_ID')
print(df_storm_bronx.shape)
 

# Loading the dataset for Manhattan

# In[16]:


df_storm_ny = pd.read_csv('storm_data_search_results_ny.csv', 
                       header = 0,
                       sep = ',', 
                       parse_dates = ['BEGIN_DATE'],
                       index_col = 'EVENT_ID')
print(df_storm_ny.shape)


# Loading the dataset for Queens

# In[17]:


df_storm_queens = pd.read_csv('storm_data_search_results_queens.csv', 
                       header = 0,
                       sep = ',', 
                       parse_dates = ['BEGIN_DATE'],
                       index_col = 'EVENT_ID')
print(df_storm_queens.shape)


# ## Preprocessing the Storms Data

# Appending the datasets

# In[18]:


df_storm = pd.concat([df_storm_ny, df_storm_bronx, df_storm_queens], ignore_index=True)
df_storm.shape


# Checking the loaded data

# In[19]:


pd.set_option('display.max_columns', None)
df_storm.head(5)


# Listing the columns against their indexes

# In[20]:


count = 0
for col in df_storm.columns:
  print(count, col)
  count+=1


# Checking for nulls

# In[21]:


null_counts = df_storm.isnull().sum()
print(null_counts)


# Checking datatypes

# In[22]:


print(df_storm.dtypes)


# Renaming columns for better understanding and easier merge

# In[23]:


df_storm = df_storm.rename(columns={'BEGIN_DATE': 'Created Date', 'CZ_NAME_STR': 'Storm_Borough'})


# ## Merging the Datasets

# In[24]:


result = pd.merge(df,df_storm[['Storm_Borough','Created Date','BEGIN_TIME','EVENT_TYPE']], on = 'Created Date', how = 'left')


# In[25]:


result.shape


# In[ ]:


df.to_csv('/data/final_dataset.csv', index=False)


# In[1]:




