# Extracted from https://stackoverflow.com/questions/20250771/remap-values-in-pandas-column-with-a-dict-preserve-nans
df['col1'].apply(lambda x: {1: "A", 2: "B"}.get(x,x))

df['col1']=df['col1'].apply(lambda x: {1: "A", 2: "B"}.get(x,x))
df
  col1 col2
0    w    a
1    1    2
2    2  NaN


