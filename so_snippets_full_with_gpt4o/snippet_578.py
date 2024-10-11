# Extracted from https://stackoverflow.com/questions/22341271/get-list-from-pandas-dataframe-column-or-row
df
  cluster load_date budget actual fixed_price
0       A  1/1/2014   1000   4000           Y
1       A  2/1/2014  12000  10000           Y
2       A  3/1/2014  36000   2000           Y
3       B  4/1/2014  15000  10000           N
4       B  4/1/2014  12000  11500           N
5       B  4/1/2014  90000  11000           N
6       C  7/1/2014  22000  18000           N
7       C  8/1/2014  30000  28960           N
8       C  9/1/2014  53000  51200           N

ser_aggCol (collapse each column to a list)
cluster          [A, A, A, B, B, B, C, C, C]
load_date      [1/1/2014, 2/1/2014, 3/1/2...
budget         [1000, 12000, 36000, 15000...
actual         [4000, 10000, 2000, 10000,...
fixed_price      [Y, Y, Y, N, N, N, N, N, N]
dtype: object


ser_aggRows (collapse each row to a list)
0     [A, 1/1/2014, 1000, 4000, Y]
1    [A, 2/1/2014, 12000, 10000...
2    [A, 3/1/2014, 36000, 2000, Y]
3    [B, 4/1/2014, 15000, 10000...
4    [B, 4/1/2014, 12000, 11500...
5    [B, 4/1/2014, 90000, 11000...
6    [C, 7/1/2014, 22000, 18000...
7    [C, 8/1/2014, 30000, 28960...
8    [C, 9/1/2014, 53000, 51200...
dtype: object


df_gr (here you get lists for each cluster)
                             load_date                 budget                 actual fixed_price
cluster                                                                                         
A        [1/1/2014, 2/1/2014, 3/1/2...   [1000, 12000, 36000]    [4000, 10000, 2000]   [Y, Y, Y]
B        [4/1/2014, 4/1/2014, 4/1/2...  [15000, 12000, 90000]  [10000, 11500, 11000]   [N, N, N]
C        [7/1/2014, 8/1/2014, 9/1/2...  [22000, 30000, 53000]  [18000, 28960, 51200]   [N, N, N]


a list of separate dataframes for each cluster

df for cluster A
  cluster load_date budget actual fixed_price
0       A  1/1/2014   1000   4000           Y
1       A  2/1/2014  12000  10000           Y
2       A  3/1/2014  36000   2000           Y

df for cluster B
  cluster load_date budget actual fixed_price
3       B  4/1/2014  15000  10000           N
4       B  4/1/2014  12000  11500           N
5       B  4/1/2014  90000  11000           N

df for cluster C
  cluster load_date budget actual fixed_price
6       C  7/1/2014  22000  18000           N
7       C  8/1/2014  30000  28960           N
8       C  9/1/2014  53000  51200           N

just the values of column load_date
0    1/1/2014
1    2/1/2014
2    3/1/2014
3    4/1/2014
4    4/1/2014
5    4/1/2014
6    7/1/2014
7    8/1/2014
8    9/1/2014
Name: load_date, dtype: object


just the values of column number 2
0     1000
1    12000
2    36000
3    15000
4    12000
5    90000
6    22000
7    30000
8    53000
Name: budget, dtype: object


just the values of row number 7
cluster               C
load_date      8/1/2014
budget            30000
actual            28960
fixed_price           N
Name: 7, dtype: object


============================== JUST FOR COMPLETENESS ==============================


you can convert a series to a list
['C', '8/1/2014', '30000', '28960', 'N']


you can convert a dataframe to a nested list
[['A', '1/1/2014', '1000', '4000', 'Y'], ['A', '2/1/2014', '12000', '10000', 'Y'], ['A', '3/1/2014', '36000', '2000', 'Y'], ['B', '4/1/2014', '15000', '10000', 'N'], ['B', '4/1/2014', '12000', '11500', 'N'], ['B', '4/1/2014', '90000', '11000', 'N'], ['C', '7/1/2014', '22000', '18000', 'N'], ['C', '8/1/2014', '30000', '28960', 'N'], ['C', '9/1/2014', '53000', '51200', 'N']]

the content of a dataframe can be accessed as a numpy.ndarray
[['A' '1/1/2014' '1000' '4000' 'Y']
 ['A' '2/1/2014' '12000' '10000' 'Y']
 ['A' '3/1/2014' '36000' '2000' 'Y']
 ['B' '4/1/2014' '15000' '10000' 'N']
 ['B' '4/1/2014' '12000' '11500' 'N']
 ['B' '4/1/2014' '90000' '11000' 'N']
 ['C' '7/1/2014' '22000' '18000' 'N']
 ['C' '8/1/2014' '30000' '28960' 'N']
 ['C' '9/1/2014' '53000' '51200' 'N']]

# prefix ser refers to pd.Series object
# prefix df refers to pd.DataFrame object
# prefix lst refers to list object

import pandas as pd
import numpy as np

df=pd.DataFrame([
        ['A',   '1/1/2014',    '1000',    '4000',    'Y'],
        ['A',   '2/1/2014',    '12000',   '10000',   'Y'],
        ['A',   '3/1/2014',    '36000',   '2000',    'Y'],
        ['B',   '4/1/2014',    '15000',   '10000',   'N'],
        ['B',   '4/1/2014',    '12000',   '11500',   'N'],
        ['B',   '4/1/2014',    '90000',   '11000',   'N'],
        ['C',   '7/1/2014',    '22000',   '18000',   'N'],
        ['C',   '8/1/2014',    '30000',   '28960',   'N'],
        ['C',   '9/1/2014',    '53000',   '51200',   'N']
        ], columns=['cluster', 'load_date',   'budget',  'actual',  'fixed_price'])
print('df',df, sep='\n', end='\n\n')

ser_aggCol=df.aggregate(lambda x: [x.tolist()], axis=0).map(lambda x:x[0])
print('ser_aggCol (collapse each column to a list)',ser_aggCol, sep='\n', end='\n\n\n')

ser_aggRows=pd.Series(df.values.tolist()) 
print('ser_aggRows (collapse each row to a list)',ser_aggRows, sep='\n', end='\n\n\n')

df_gr=df.groupby('cluster').agg(lambda x: list(x))
print('df_gr (here you get lists for each cluster)',df_gr, sep='\n', end='\n\n\n')

lst_dfFiltGr=[ df.loc[df['cluster']==val,:] for val in df['cluster'].unique() ]
print('a list of separate dataframes for each cluster', sep='\n', end='\n\n')
for dfTmp in lst_dfFiltGr:
    print('df for cluster '+str(dfTmp.loc[dfTmp.index[0],'cluster']),dfTmp, sep='\n', end='\n\n')

ser_singleColLD=df.loc[:,'load_date']
print('just the values of column load_date',ser_singleColLD, sep='\n', end='\n\n\n')

ser_singleCol2=df.iloc[:,2]
print('just the values of column number 2',ser_singleCol2, sep='\n', end='\n\n\n')

ser_singleRow7=df.iloc[7,:]
print('just the values of row number 7',ser_singleRow7, sep='\n', end='\n\n\n')

print('='*30+' JUST FOR COMPLETENESS '+'='*30, end='\n\n\n')

lst_fromSer=ser_singleRow7.tolist()
print('you can convert a series to a list',lst_fromSer, type(lst_fromSer), sep='\n', end='\n\n\n')

lst_fromDf=df.values.tolist()
print('you can convert a dataframe to a nested list',lst_fromDf, type(lst_fromDf), sep='\n', end='\n\n')

arr_fromDf=df.values
print('the content of a dataframe can be accessed as a numpy.ndarray',arr_fromDf, type(arr_fromDf), sep='\n', end='\n\n')

