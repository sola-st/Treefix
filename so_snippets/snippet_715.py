# Extracted from https://stackoverflow.com/questions/17134716/convert-dataframe-column-type-from-string-to-datetime
df['col'] = pd.to_datetime(df['col'])

In [11]: pd.to_datetime(pd.Series(['05/23/2005']))
Out[11]:
0   2005-05-23 00:00:00
dtype: datetime64[ns]

In [12]: pd.to_datetime(pd.Series(['05/23/2005']), format="%m/%d/%Y")
Out[12]:
0   2005-05-23
dtype: datetime64[ns]

