# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#38798
max_val = np.iinfo(np.uint64).max - 1
result = Series([max_val, val], dtype="UInt64")
expected = Series(np.array([max_val, 1], dtype="uint64"), dtype="UInt64")
tm.assert_series_equal(result, expected)
