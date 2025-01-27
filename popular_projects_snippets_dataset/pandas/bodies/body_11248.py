# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
df.columns = np.arange(len(df.columns))

# it works!
df.groupby(1, as_index=False)[2].agg({"Q": np.mean})
