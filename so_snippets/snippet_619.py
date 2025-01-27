# Extracted from https://stackoverflow.com/questions/21800169/python-pandas-get-index-of-rows-where-column-matches-certain-value
df.index[df['BoolCol'] == True].tolist()

df.index[df['BoolCol']].tolist()

df = pd.DataFrame({'BoolCol': [True, False, False, True, True]},
       index=[10,20,30,40,50])

In [53]: df
Out[53]: 
   BoolCol
10    True
20   False
30   False
40    True
50    True

[5 rows x 1 columns]

In [54]: df.index[df['BoolCol']].tolist()
Out[54]: [10, 40, 50]

In [56]: idx = df.index[df['BoolCol']]

In [57]: idx
Out[57]: Int64Index([10, 40, 50], dtype='int64')

In [58]: df.loc[idx]
Out[58]: 
   BoolCol
10    True
40    True
50    True

[3 rows x 1 columns]

In [55]: df.loc[df['BoolCol']]
Out[55]: 
   BoolCol
10    True
40    True
50    True

[3 rows x 1 columns]

In [110]: np.flatnonzero(df['BoolCol'])
Out[112]: array([0, 3, 4])

In [113]: df.iloc[np.flatnonzero(df['BoolCol'])]
Out[113]: 
   BoolCol
10    True
40    True
50    True

