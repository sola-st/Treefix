# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# GH#8131
df = DataFrame({"c_1": ["a", "b", "c"], "n_1": [1.0, 2.0, 3.0]})
sp_array = SparseArray([0, 0, 1])
df["new_column"] = sp_array

expected = Series(sp_array, name="new_column")
tm.assert_series_equal(df["new_column"], expected)
