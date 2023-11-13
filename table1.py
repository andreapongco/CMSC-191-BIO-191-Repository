import pandas as pd
import random

df = pd.read_csv('table1.csv')

df.insert(0, "id", range(1, len(df)+1))
df['Date'] = "META-" + df['Date']
df.insert(2, "Random", [random.randint(0, 1) for i in range(0, len(df))])


df.to_csv('table2.csv', index=False)