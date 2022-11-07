import pandas as pd

df = pd.read_csv("vtb2.csv")
result = df.groupby('UserID', as_index = False).aggregate({"ViewDate": 'count'}).sort_values("ViewDate", ascending=False).reset_index(drop=True)

print(result.head(10))