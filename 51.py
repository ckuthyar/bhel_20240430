import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data2.csv")
info1['Date']=pd.to_datetime(info1['Date'])    
print(info1.to_string())
