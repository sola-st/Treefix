# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
df = DataFrame({"c_1": ["a", "b", "c"], "n_1": [1.0, 2.0, 3.0]})
sp_series = Series(SparseArray([0, 0, 1]), index=[2, 1, 0])

df["new_column"] = sp_series
expected = Series(SparseArray([1, 0, 0]), name="new_column")
tm.assert_series_equal(df["new_column"], expected)
