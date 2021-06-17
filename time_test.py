
import datetime
import time
import pandas as pd
import numpy as np
import os


for i in range(100):
    a = i * 2
    time.sleep(1)
    print(a)
    now = datetime.datetime.now()
    df = pd.DataFrame({
    'value':a,
    'time':[now]})
    df.to_csv("dfdf.csv", mode = "a", header=False)
