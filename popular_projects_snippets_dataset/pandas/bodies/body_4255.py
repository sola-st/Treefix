# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
df = DataFrame(np.random.randn(5, 3))
# NA
df.loc[0, 0] = np.nan
rs = df.eq(df)
assert not rs.loc[0, 0]
rs = df.ne(df)
assert rs.loc[0, 0]
rs = df.gt(df)
assert not rs.loc[0, 0]
rs = df.lt(df)
assert not rs.loc[0, 0]
rs = df.ge(df)
assert not rs.loc[0, 0]
rs = df.le(df)
assert not rs.loc[0, 0]
