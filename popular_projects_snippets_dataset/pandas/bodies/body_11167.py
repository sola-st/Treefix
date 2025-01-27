# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH#44417
df = DataFrame(np.random.randn(0, 4))
df[3] = df[3].astype(np.int64)
df.columns = [0, 1, 2, 0]
gb = df.groupby(df[1], group_keys=False)
res = gb.apply(lambda x: x)
assert (res.dtypes == df.dtypes).all()
