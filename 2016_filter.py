import pandas as pd

df = pd.read_csv("dataCleaned1.csv", low_memory=False)

filtered_df = df.loc[(df['Date'] >= '2016-01-01')]

filtered_df.to_csv("2016_and_on.csv")