import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data2.csv")
print(info1.duplicated())
