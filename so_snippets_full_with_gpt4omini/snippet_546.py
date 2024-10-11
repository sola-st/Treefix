# Extracted from https://stackoverflow.com/questions/37787698/how-to-sort-pandas-dataframe-from-one-column
df.sort_values(by=['2'], inplace=True)

# or

df.sort_values(by = '2', inplace = True)

# or

df.sort_values('2', inplace = True)

df = df.sort_values(by=['2'])

df_new = df.sort_values(by=['2'])

        0          1     2
4    85.6    January   1.0
3    95.5   February   2.0
7   104.8      March   3.0
0   354.7      April   4.0
8   283.5        May   5.0
6   238.7       June   6.0
5     152       July   7.0
1    55.4     August   8.0
11  212.7  September   9.0
10  249.6    October  10.0
9   278.8   November  11.0
2   176.5   December  12.0

df.reset_index(drop = True, inplace = True)

# or

df = df.reset_index(drop = True)

[Out]:

        0          1     2
0    85.6    January   1.0
1    95.5   February   2.0
2   104.8      March   3.0
3   354.7      April   4.0
4   283.5        May   5.0
5   238.7       June   6.0
6     152       July   7.0
7    55.4     August   8.0
8   212.7  September   9.0
9   249.6    October  10.0
10  278.8   November  11.0
11  176.5   December  12.0

df = df.sort_values(by=['2']).reset_index(drop = True)

[Out]:

        0          1     2
0    85.6    January   1.0
1    95.5   February   2.0
2   104.8      March   3.0
3   354.7      April   4.0
4   283.5        May   5.0
5   238.7       June   6.0
6     152       July   7.0
7    55.4     August   8.0
8   212.7  September   9.0
9   249.6    October  10.0
10  278.8   November  11.0
11  176.5   December  12.0

 df['2'] = pd.to_numeric(df['2'])

 df['2'] = df['2'].astype(float)

 df = df.sort_values(by=['2'], ascending=False)

 # or

 df.sort_values(by = '2', ascending=False, inplace=True)

 [Out]:

        0          1     2
2   176.5   December  12.0
9   278.8   November  11.0
10  249.6    October  10.0
11  212.7  September   9.0
1    55.4     August   8.0
5     152       July   7.0
6   238.7       June   6.0
8   283.5        May   5.0
0   354.7      April   4.0
7   104.8      March   3.0
3    95.5   February   2.0
4    85.6    January   1.0

