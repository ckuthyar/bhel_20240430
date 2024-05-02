import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data2.csv")
info1.loc[7,"Duration"]=45
print(info1.to_string())
