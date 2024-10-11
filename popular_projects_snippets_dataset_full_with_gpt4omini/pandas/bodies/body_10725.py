# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
df = DataFrame(np.random.randn(1000))
df.values[::2] = np.nan

labels = np.random.randint(0, 50, size=1000).astype(float)
labels[::17] = np.nan

result = df.groupby(labels).median()
exp = df.groupby(labels).agg(nanops.nanmedian)
tm.assert_frame_equal(result, exp)

df = DataFrame(np.random.randn(1000, 5))
rs = df.groupby(labels).agg(np.median)
xp = df.groupby(labels).median()
tm.assert_frame_equal(rs, xp)
