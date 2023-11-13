"""
Author: Andrea Kristine S. Pongco
Date of Development: Novmber 13, 2023
"""

import pandas as pd
import random

df = pd.read_csv('table1.csv') #read csv file

df.insert(0, "id", range(1, len(df)+1)) #insert column "id" with values ranging from 1 to len(df)
df['Date'] = "META-" + df['Date'] #modify column 2 (Date) and add a prefix "META-"
df.insert(2, "Random", [random.randint(0, 1) for i in range(0, len(df))]) #add a third column that has values randomly generated from 0 to 1
df = df.T #transpose the data

df.to_csv('table3.csv', index=False)