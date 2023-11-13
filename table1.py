import pandas as pd

df = pd.read_csv('table1.csv')

df['id'] = range(1, len(df)+1)

print(df.head())