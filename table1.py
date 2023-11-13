import pandas as pd

df = pd.read_csv('table1.csv')

df.insert(0, "id", range(1, len(df)+1))
df['Date'] = "META-" + df['Date']


df.to_csv('table1.csv', index=False)