import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data1.csv")
info1.corr()
print(info1)
