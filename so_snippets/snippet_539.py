# Extracted from https://stackoverflow.com/questions/12065885/filter-dataframe-rows-if-value-in-column-is-in-a-set-list-of-values
    RPT_Date  STK_ID STK_Name  sales
0 1980-01-01       0   Arthur      0
1 1980-01-02       1    Beate      4
2 1980-01-03       2    Cecil      2
3 1980-01-04       3     Dana      8
4 1980-01-05       4     Eric      4
5 1980-01-06       5    Fidel      5
6 1980-01-07       6   George      4
7 1980-01-08       7     Hans      7
8 1980-01-09       8   Ingrid      7
9 1980-01-10       9    Jones      4

mask = df['STK_ID'].isin([4, 2, 6])

mask
0    False
1    False
2     True
3    False
4     True
5    False
6     True
7    False
8    False
9    False
Name: STK_ID, dtype: bool

df[mask]
    RPT_Date  STK_ID STK_Name  sales
2 1980-01-03       2    Cecil      2
4 1980-01-05       4     Eric      4
6 1980-01-07       6   George      4

df.set_index('STK_ID', inplace=True)
         RPT_Date STK_Name  sales
STK_ID                           
0      1980-01-01   Arthur      0
1      1980-01-02    Beate      4
2      1980-01-03    Cecil      2
3      1980-01-04     Dana      8
4      1980-01-05     Eric      4
5      1980-01-06    Fidel      5
6      1980-01-07   George      4
7      1980-01-08     Hans      7
8      1980-01-09   Ingrid      7
9      1980-01-10    Jones      4

df.loc[[4, 2, 6]]
         RPT_Date STK_Name  sales
STK_ID                           
4      1980-01-05     Eric      4
2      1980-01-03    Cecil      2
6      1980-01-07   George      4

stkid_df = pd.DataFrame({"STK_ID": [4,2,6]})
df.merge(stkid_df, on='STK_ID')
   STK_ID   RPT_Date STK_Name  sales
0       2 1980-01-03    Cecil      2
1       4 1980-01-05     Eric      4
2       6 1980-01-07   George      4

