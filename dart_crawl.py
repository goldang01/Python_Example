#!/usr/bin/env python
# coding: utf-8

# In[2]:


# OpenDartReader를 사용한 Dart 재무제표 수집
import datetime
import time
import pandas as pd
import numpy as np
import OpenDartReader
import os
import sys


# In[ ]:


argv_value_1 = sys.argv[1] # date start
argv_value_2 = sys.argv[2] # date end
argv_value_3 = sys.argv[3] # report type
argv_value_4 = sys.argv[4] # api key


# In[4]:


# ==== 0. 객체 생성 ====
# 객체 생성 (API KEY 지정) 
api_key = argv_value_4

dart = OpenDartReader(api_key) 


# In[6]:


report_list = dart.list(start=argv_value_1, end=argv_value_2, kind='A')
corp_list = report_list['corp_name']


# In[12]:


# 파일명

file_name = "file_" + argv_value_1 + "_" + argv_value_2 + "_" + argv_value_3 + ".csv"
time_log = "log_" + argv_value_1 + "_" + argv_value_2 + "_" + argv_value_3 + ".csv"


# In[13]:


for i in corp_list:
    # 분당 100개 제한 관련 함수
    time.sleep(3)
    
    # log 에 찍을 시각
    now = datetime.datetime.now()
    
    # 21년도 재무재표 수집
    try:
        df1 = dart.finstate(i, 2021, reprt_code=argv_value_3)
    except Exception as e:
        df_log = pd.DataFrame({
            'TF': '회사명 에러',
            '회사이름':i,
            'time':[now]})
    
        df_log.to_csv(time_log, index=False, mode = "a", header=False)

    if df1 is None:
        # 데이터 존재 하지 않을 경우 로그    
        df_log = pd.DataFrame({
            'TF':"존재하지 않음",
            '회사이름':i,
            'time':[now]})
    
        df_log.to_csv(time_log, index=False, mode = "a", header=False)
    else:
        # 데이터가 존재할경우 csv에 저장
        if not os.path.exists(file_name):
            df1.to_csv(file_name, index=False, mode='w')
        else:
            df1.to_csv(file_name, index=False, mode='a', header=False)

            df_log = pd.DataFrame({
                'TF':"성공",
                '회사이름':i,
                'time':[now]})
            df_log.to_csv(time_log, index=False, mode = "a", header=False)

