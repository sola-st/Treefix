# Extracted from https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression
df = df.drop(some labels)
df = df.drop(df[<some boolean condition>].index)

df = df.drop(df[df.score < 50].index)

df.drop(df[df.score < 50].index, inplace=True)

df = df.drop(df[(df.score < 50) & (df.score > 20)].index)

