import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('Strom.xlsx', sheet_name='Tabellenblatt1')

print("Column headings:")
print(df.columns)

df_new = df.copy()
df_new['datum'] = pd.to_datetime(df_new['datum'])
df_new.index = df_new['datum']

df_interpol = df_new.resample('D').mean()
df_interpol['1.8.0'] = df_interpol['1.8.0'].interpolate()
df_interpol['1.8.1'] = df_interpol['1.8.1'].interpolate()
df_interpol['1.8.2'] = df_interpol['1.8.2'].interpolate()
df_interpol.head(40)

df_interpol.to_excel("output.xlsx")
