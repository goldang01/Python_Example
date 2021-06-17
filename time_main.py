#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Dart 재무재표 수집


# In[ ]:


import os
import time
import pandas as pd


# In[22]:


date_list_start = ["20210101", "20210401"]
date_list_end = ["20210331", "20210615"]

apikey = [
    "052b7f6184ff2b9576d64eedb735f904aacb28f4", # 네이버 계정
    "609b5ce551ea756056d4cb656d90fdc3f589a4e1" # google 계정
]

# 1분기보고서 : 11013
# 반기보고서 : 11012
# 3분기보고서 : 11014
# 사업보고서 : 11011

report_type = ["11013", "11012", "11014", "11011"]

for j in range(2):
    for i in report_type:
        os.system("/usr/bin/python3 /home/ubuntu/python/Python_Example/dart_crawl.py" + " " + date_list_start[j] + " " + date_list_end[j] + " " +  i + " " + apikey[j])

