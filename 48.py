import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data1.csv")
cals=info1["Calories"].mean()
info1["Calories"].fillna(cals,inplace=True)
print(info1.to_string())
