from efficient_apriori import apriori
import csv
import pandas as pd
from datetime import datetime

df = pd.read_csv('dataCleaned1.csv', low_memory=False)

df= df.drop("Fine",axis=1)
df= df.drop("Discounted Fine",axis=1)
df= df.drop(" Violation Description",axis=1)

df['Date2'] = pd.to_datetime(df['Date'])     # skip if your Date column already in datetime format
df['Day of Week'] = df['Date2'].dt.dayofweek
df['Date'] = df['Date2'].dt.year

df= df.drop("Date2",axis=1)
df= df.drop("Time",axis=1)
df.to_csv("apriori_cleaned_data.csv", index=False)


