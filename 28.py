import pandas as pd
gym={
    "calories":[420,380,390],
    "duration":[50,40,45]
    }
info1=pd.DataFrame(gym, index=["CS","Kishan","Shashank"])
print(info1.loc["Kishan"])
