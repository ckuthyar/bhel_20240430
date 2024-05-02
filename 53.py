import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data2.csv")
info1.dropna(subset=['Date'],inplace=True)
print(info1.to_string())
