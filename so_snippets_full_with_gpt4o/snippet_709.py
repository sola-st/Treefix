# Extracted from https://stackoverflow.com/questions/17141558/how-to-sort-a-dataframe-in-python-pandas-by-two-or-more-columns
df.sort_values(['a', 'b'], ascending=[True, False])

df.sort(['a', 'b'], ascending=[True, False])

In [11]: df1 = pd.DataFrame(np.random.randint(1, 5, (10,2)), columns=['a','b'])

In [12]: df1.sort(['a', 'b'], ascending=[True, False])
Out[12]:
   a  b
2  1  4
7  1  3
1  1  2
3  1  2
4  3  2
6  4  4
0  4  3
9  4  3
5  4  1
8  4  1

df1 = df1.sort(['a', 'b'], ascending=[True, False])

df1.sort(['a', 'b'], ascending=[True, False], inplace=True)

