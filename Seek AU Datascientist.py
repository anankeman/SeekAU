
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import os


# In[3]:

ruta = pd.read_csv('C:/Users/Pippo/Documents/Python Scripts/seekau/test3.csv')


# In[10]:

ruta


# In[4]:

lugar = ruta['place'].copy()
categoria1 = ruta['category'].copy()
categoria2 = ruta['category2'].copy()


# In[12]:

lugar


# In[19]:

pivot = lugar.value_counts()


# In[20]:

pivot


# In[32]:

pivot.plot(kind="bar")


# In[31]:

categoria1.value_counts().plot(kind="bar")


# In[33]:

categoria2.value_counts().plot(kind="bar")


# In[5]:

ruta[["category","category2"]]

