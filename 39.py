import pandas as pd
import matplotlib.pyplot as plt
info1=pd.read_csv("data1.csv")
info1['Duration'].plot(kind='hist')
plt.show()
  
