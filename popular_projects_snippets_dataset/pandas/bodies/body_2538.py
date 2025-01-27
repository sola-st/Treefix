# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#36319
cols = Index([1, 2, 3], dtype=dtype)
df = DataFrame(np.random.randn(3, 3), columns=cols)

df[False] = ["a", "b", "c"]

expected_cols = Index([1, 2, 3, False], dtype=object)
if dtype == "f8":
    expected_cols = Index([1.0, 2.0, 3.0, False], dtype=object)

tm.assert_index_equal(df.columns, expected_cols)
