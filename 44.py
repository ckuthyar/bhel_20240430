import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data1.csv")
info2=info1.fillna(9999) #Fill empty cells with 9999
print(info2.to_string())
