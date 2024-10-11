# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#19920
columns = Index([100, 200, 300], dtype=np.uint64, name="foo")
df = DataFrame(np.arange(15).reshape(5, 3), columns=columns)
df = df.astype(dtype)
tm.assert_index_equal(df.columns, columns)
