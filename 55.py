import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data2.csv")
for x in info1.index:
    if info1.loc[x,"Duration"]>120:
          info1.loc[x,"Duration"]=120
print(info1.to_string())
