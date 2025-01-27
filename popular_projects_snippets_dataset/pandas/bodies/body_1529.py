# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH34687
s = Series([1.0, 0.0, 0.0, 0.0, 0.0], dtype=SparseDtype("float64", 0.0))

result = s.loc[range(2)]
expected = Series([1.0, 0.0], dtype=SparseDtype("float64", 0.0))
tm.assert_series_equal(result, expected)

result = s.loc[range(3)].loc[range(2)]
expected = Series([1.0, 0.0], dtype=SparseDtype("float64", 0.0))
tm.assert_series_equal(result, expected)
