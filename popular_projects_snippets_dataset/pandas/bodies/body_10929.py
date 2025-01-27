# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
arr = list(map(df.index.get_level_values, range(df.index.nlevels)))
df.index = MultiIndex.from_arrays(arr, names=df.index.names)
exit(df)
