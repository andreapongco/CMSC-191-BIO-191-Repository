import pandas as pd
import random

df = pd.read_csv('table1.csv')

df.insert(0, "id", range(1, len(df)+1))
df['Date'] = "META-" + df['Date']
df.insert(2, "Random", random.randint(0, 2))


df.to_csv('table2.csv', index=False)