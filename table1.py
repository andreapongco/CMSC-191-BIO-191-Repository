import pandas as pd

df = pd.read_csv('table1.csv')

#df['id'] = range(1, len(df)+1)

df.insert(0, "id'", range(1, len(df)+1)) 

df.to_csv('table1.csv', index=False)