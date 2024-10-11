# Extracted from https://stackoverflow.com/questions/22391433/count-the-frequency-that-a-value-occurs-in-a-dataframe-column
In [37]:
df = pd.DataFrame({'a':list('abssbab')})
df['a'].value_counts()

Out[37]:

b    3
a    2
s    2
dtype: int64

In [38]:
df.groupby('a').count()

Out[38]:

   a
a   
a  2
b  3
s  2

[3 rows x 1 columns]

In [41]:
df['freq'] = df.groupby('a')['a'].transform('count')
df

Out[41]:

   a freq
0  a    2
1  b    3
2  s    2
3  s    2
4  b    3
5  a    2
6  b    3

[7 rows x 2 columns]

