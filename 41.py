import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data1.csv")
info2=info1.dropna()  #drop rows with empty cells
print(info2.to_string())
