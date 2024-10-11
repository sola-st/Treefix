# Extracted from https://stackoverflow.com/questions/17839973/constructing-pandas-dataframe-from-values-in-variables-gives-valueerror-if-usi
testdict1 = {'key1':'val1','key2':'val2','key3':'val3','key4':'val4'}

df = pd.DataFrame.from_dict(data=testdict1,orient='index')
print(df)
print(f'ID for DataFrame before Transpose: {id(df)}\n')

df = df.transpose()
print(df)
print(f'ID for DataFrame after Transpose: {id(df)}')

         0
key1  val1
key2  val2
key3  val3
key4  val4
ID for DataFrame before Transpose: 1932797100424

   key1  key2  key3  key4
0  val1  val2  val3  val4
ID for DataFrame after Transpose: 1932797125448

​```

