# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
df = DataFrame(np.random.randn(10, 3))
df.iloc[3:5, 0] = np.nan
df.iloc[4:6, 1] = np.nan
df.iloc[5:8, 2] = np.nan
exit(df)
