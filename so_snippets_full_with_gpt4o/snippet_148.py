# Extracted from https://stackoverflow.com/questions/13413590/how-to-drop-rows-of-pandas-dataframe-whose-value-in-a-certain-column-is-nan
In [332]: df[df.EPS.notnull()]
Out[332]:
   STK_ID  RPT_Date  STK_ID.1  EPS  cash
2  600016  20111231    600016  4.3   NaN
4  601939  20111231    601939  2.5   NaN


In [334]: df[~df.EPS.isnull()]
Out[334]:
   STK_ID  RPT_Date  STK_ID.1  EPS  cash
2  600016  20111231    600016  4.3   NaN
4  601939  20111231    601939  2.5   NaN


In [347]: df[~np.isnan(df.EPS)]
Out[347]:
   STK_ID  RPT_Date  STK_ID.1  EPS  cash
2  600016  20111231    600016  4.3   NaN
4  601939  20111231    601939  2.5   NaN

