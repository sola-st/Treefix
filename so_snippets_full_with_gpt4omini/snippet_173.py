# Extracted from https://stackoverflow.com/questions/12555323/how-to-add-a-new-column-to-an-existing-dataframe
df['e'] = e.values

df1 = df1.assign(e=e.values)

df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df.assign(mean_a=df.a.mean(), mean_b=df.b.mean())
   a  b  mean_a  mean_b
0  1  3     1.5     3.5
1  2  4     1.5     3.5

np.random.seed(0)
df1 = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
mask = df1.applymap(lambda x: x <-0.7)
df1 = df1[-mask.any(axis=1)]
sLength = len(df1['a'])
e = pd.Series(np.random.randn(sLength))

df1
          a         b         c         d
0  1.764052  0.400157  0.978738  2.240893
2 -0.103219  0.410599  0.144044  1.454274
3  0.761038  0.121675  0.443863  0.333674
7  1.532779  1.469359  0.154947  0.378163
9  1.230291  1.202380 -0.387327 -0.302303

e
0   -1.048553
1   -1.420018
2   -1.706270
3    1.950775
4   -0.509652
dtype: float64

df1 = df1.assign(e=e.values)

df1
          a         b         c         d         e
0  1.764052  0.400157  0.978738  2.240893 -1.048553
2 -0.103219  0.410599  0.144044  1.454274 -1.420018
3  0.761038  0.121675  0.443863  0.333674 -1.706270
7  1.532779  1.469359  0.154947  0.378163  1.950775
9  1.230291  1.202380 -0.387327 -0.302303 -0.509652

