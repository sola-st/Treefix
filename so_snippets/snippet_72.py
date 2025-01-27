# Extracted from https://stackoverflow.com/questions/13411544/delete-a-column-from-a-pandas-dataframe
df.drop(df.columns[[0,1,3]], axis=1, inplace=True)

df.drop(df.columns[[0]], axis=1, inplace=True)

df.pop('column-name')

df = DataFrame.from_items([('A', [1, 2, 3]), ('B', [4, 5, 6]), ('C', [7,8, 9])], orient='index', columns=['one', 'two', 'three'])

   one  two  three
A    1    2      3
B    4    5      6
C    7    8      9

   two  three
A    2      3
B    5      6
C    8      9

   two
A    2
B    5
C    8

