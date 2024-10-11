# Extracted from https://stackoverflow.com/questions/11869910/pandas-filter-rows-of-dataframe-with-operator-chaining
In [96]: df
Out[96]:
   A  B  C  D
a  1  4  9  1
b  4  5  0  2
c  5  5  1  0
d  1  3  9  6

In [99]: df[(df.A == 1) & (df.D == 6)]
Out[99]:
   A  B  C  D
d  1  3  9  6

df[((df.A==1) == True) | ((df.D==6) == True)]

