# Extracted from https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-and-then-filling-it
data = []
for row in some_function_that_yields_data():
    data.append(row)

df = pd.DataFrame(data)

df = pd.DataFrame(columns=['A', 'B', 'C'])
for a, b, c in some_function_that_yields_data():
    df = df.append({'A': i, 'B': b, 'C': c}, ignore_index=True) # yuck
    # or similarly,
    # df = pd.concat([df, pd.Series({'A': i, 'B': b, 'C': c})], ignore_index=True)

df = pd.DataFrame(columns=['A', 'B', 'C'])
df = df.append({'A': 1, 'B': 12.3, 'C': 'xyz'}, ignore_index=True)

df.dtypes
A     object   # yuck!
B    float64
C     object
dtype: object

df.infer_objects().dtypes
A      int64
B    float64
C     object
dtype: object

df = pd.DataFrame(columns=['A', 'B', 'C'])
for a, b, c in some_function_that_yields_data():
    df.loc[len(df)] = [a, b, c]

df = pd.DataFrame(columns=['A', 'B', 'C'], index=range(5))
df
     A    B    C
0  NaN  NaN  NaN
1  NaN  NaN  NaN
2  NaN  NaN  NaN
3  NaN  NaN  NaN
4  NaN  NaN  NaN

df.dtypes
A    object  # you DON'T want this
B    object
C    object
dtype: object

for i, (a, b, c) in enumerate(some_function_that_yields_data()):
    df.iloc[i] = [a, b, c]

