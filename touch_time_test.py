#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import pandas as pd
now = datetime.datetime.now()
df = pd.DataFrame({
    "time":[now]
})
df.to_csv("time_test.csv", mode = "a")

