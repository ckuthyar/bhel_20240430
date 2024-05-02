import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data1.csv")
info1.dropna(inplace=True) #we are changing the original dataframe
print(info1.to_string())
