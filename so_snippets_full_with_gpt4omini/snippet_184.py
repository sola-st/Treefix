# Extracted from https://stackoverflow.com/questions/12096252/use-a-list-of-values-to-select-rows-from-a-pandas-dataframe
In [1]: df = pd.DataFrame({'A': [5,6,3,4], 'B': [1,2,3,5]})

In [2]: df
Out[2]:
   A  B
0  5  1
1  6  2
2  3  3
3  4  5

In [3]: df[df['A'].isin([3, 6])]
Out[3]:
   A  B
1  6  2
2  3  3

In [4]: df[~df['A'].isin([3, 6])]
Out[4]:
   A  B
0  5  1
3  4  5

