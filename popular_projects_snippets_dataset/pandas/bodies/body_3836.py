# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# See gh-12344
warn = None
msg = "will attempt to set the values inplace"

df = DataFrame(np.arange(9).reshape(3, 3).T)
df.columns = list("AAA")
expected = df.iloc[:, 2]

with tm.assert_produces_warning(warn, match=msg):
    df.iloc[:, 0] = 3
tm.assert_series_equal(df.iloc[:, 2], expected)

df = DataFrame(np.arange(9).reshape(3, 3).T)
df.columns = [2, float(2), str(2)]
expected = df.iloc[:, 1]

with tm.assert_produces_warning(warn, match=msg):
    df.iloc[:, 0] = 3
tm.assert_series_equal(df.iloc[:, 1], expected)
