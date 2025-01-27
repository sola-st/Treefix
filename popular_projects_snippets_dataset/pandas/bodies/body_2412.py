# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame(np.random.randn(10, 5))

# this is OK
result = df.iloc[:8:2]  # noqa
df.iloc[:8:2] = np.nan
assert isna(df.iloc[:8:2]).values.all()
