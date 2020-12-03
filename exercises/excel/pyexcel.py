"""Using python with Excel to analyze data."""

__author__ = "matthewberry5"

import pandas as pd 


df_excel = pd.read_excel('data/regions.xlsx')
df_csv = pd.read_csv('data/Names.csv')

# print(df_excel)
# print(df_csv)

df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Area Code']

# print(df_csv['Last'][0:3])

# print(df_csv.iloc[2, 1])

#Use to_excel to save an excel file with desired data columns.
# wanted_values = df_csv[['First', 'Last', 'Address']]
# stored = wanted_values.to_excel('data/State_Location.xlsx')

