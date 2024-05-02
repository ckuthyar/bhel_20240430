import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data1.csv")
info1.fillna(8888,inplace=True) #Fill empty cells with 8888 in same df
print(info1.to_string())
