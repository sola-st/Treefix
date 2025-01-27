# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH 13934
df = DataFrame({"a": [1, 2, 3]})
a = df.a
df.drop(["a"], axis=1, inplace=True)
tm.assert_index_equal(df.columns, Index([], dtype="object"))
a -= a.mean()
tm.assert_index_equal(df.columns, Index([], dtype="object"))
