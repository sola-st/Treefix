# Extracted from https://stackoverflow.com/questions/17071871/how-do-i-select-rows-from-a-dataframe-based-on-column-values
In [167]: n = 10

In [168]: df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc'))

In [169]: df
Out[169]:
          a         b         c
0  0.687704  0.582314  0.281645
1  0.250846  0.610021  0.420121
2  0.624328  0.401816  0.932146
3  0.011763  0.022921  0.244186
4  0.590198  0.325680  0.890392
5  0.598892  0.296424  0.007312
6  0.634625  0.803069  0.123872
7  0.924168  0.325076  0.303746
8  0.116822  0.364564  0.454607
9  0.986142  0.751953  0.561512

# pure python
In [170]: df[(df.a < df.b) & (df.b < df.c)]
Out[170]:
          a         b         c
3  0.011763  0.022921  0.244186
8  0.116822  0.364564  0.454607

# query
In [171]: df.query('(a < b) & (b < c)')
Out[171]:
          a         b         c
3  0.011763  0.022921  0.244186
8  0.116822  0.364564  0.454607

exclude = ('red', 'orange')
df.query('color not in @exclude')

