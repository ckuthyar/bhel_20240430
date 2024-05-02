import pandas as pd
pd.options.display.max_rows=60
info1=pd.read_json("data1.json")
print(info1.tail(20))
